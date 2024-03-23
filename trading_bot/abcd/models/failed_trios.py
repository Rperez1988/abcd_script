class Failed_Trios:

    def __init__(self, trio_ID, failed_reason) -> None:
        self.trio_ID = trio_ID
        self.failed_reason = failed_reason

    def __str__(self):
        return f"Failed_Trios(trio_ID: {self.trio_ID}, failed_reason: {self.failed_reason})"
