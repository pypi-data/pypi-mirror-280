import requests
from dataclasses import dataclass
import typing
import logging

log = logging.getLogger('sonnylabs')

URL = "https://app.sonnylabs.ai"
CONNECT_TIMEOUT = 0.5
READ_TIMEOUT = 5

DEFAULT_THRESHOLD = 0.5
THRESHOLDS = {"prompt_injection": 0.6}


@dataclass
class Scores:
    error: typing.Optional[typing.Any]
    scores: typing.Dict[str,str]

    def __bool__(self):
        """
        Return True if there are no errors, and all scores are below
        the defined thresholds
        """

        if self.error is not None:
            return False

        for name,score in self.scores.items():
            # Get user-defined threshold. Fallback to global default.
            threshold = THRESHOLDS.get(name, DEFAULT_THRESHOLD)
            if score >= threshold:
                return False

        # No errors, all scores below threshold
        return True


def score_prompt(prompt: str, analysis_id: int, tag: str, api_key: str) -> Scores:
    try:
        res = requests.post(
            f"{URL}/v1/analysis/{analysis_id}",
            params={"tag": tag},
            data=prompt,
            headers={'Authorization': f'Bearer {api_key}'},
            timeout=(CONNECT_TIMEOUT, READ_TIMEOUT)
        )

        if res.status_code >= 200 and res.status_code < 300:
            return Scores(
                error = None,
                scores = res.json(),
            )
        else:
            log.error("score_prompt API status %s", res.status_code)
            return Scores(
                error = res,
                scores = {},
            )

    except Exception as e:
        log.error("score_prompt API error %s", e)
        return Scores(
            error = e,
            scores = {},
        )
