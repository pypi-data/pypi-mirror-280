from typing import Sequence
from ewokscore import Task


class PickScan(
    Task,
    input_names=["filename", "scan_number"],
    output_names=["scan_uri"],
):
    def run(self):
        filename: Sequence[str] = self.inputs.filename
        scan_number: Sequence[int] = self.inputs.scan_number
        self.outputs.scan_uri = f"{filename}::/{scan_number}.1"
