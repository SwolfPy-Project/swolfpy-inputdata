from pathlib import Path

from .CommonData import CommonData
from .InputData import InputData


class HC_Input(InputData):
    def __init__(
        self,
        input_data_path=None,
        process_data_path=None,
        process_name="Home Composting",
        CommonDataObjct=None,
    ):
        if input_data_path:
            self.input_data_path = input_data_path
        else:
            self.input_data_path = Path(__file__).parent / "Data/HC_Input.csv"

        # Initialize the superclass
        super().__init__(self.input_data_path, process_name)

        if not CommonDataObjct:
            CommonDataObjct = CommonData()

        if process_data_path is None:
            process_data_path = Path(__file__).parent / "Data/HC_Input_MaterialDependent.csv"
        self.add_process_data(process_data_path=process_data_path, index=CommonDataObjct.Index)
