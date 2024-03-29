from pathlib import Path

from .CommonData import CommonData
from .InputData import InputData


class TS_Input(InputData):
    def __init__(self, input_data_path=None, process_name="TS", CommonDataObjct=None):
        if input_data_path:
            self.input_data_path = input_data_path
        else:
            self.input_data_path = Path(__file__).parent / "data/TS_Input.csv"

        # Initialize the superclass
        super().__init__(self.input_data_path, process_name)

        if not CommonDataObjct:
            CommonDataObjct = CommonData()
