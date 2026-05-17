class ProcessMemoqTerminology:

    def __init__(self, file_paths):
        self.file_paths = file_paths
        self.terminology_merged = terminology_merged

    def __check_file(self, file_paths):
        import os
        file_ext = os.path.splitext(file_paths[:])
        if file_ext != [".xlsx", ".csv"]:
            raise ValueError('No .xlsx or .csv files detected.')

    def import_xlsx(self, file_paths):
        xlsx_df = pd.DataFrame.import_excel(file_paths)
        return xlsx_df

    def import_csv(self, file_paths):
        csv_df = pd.DataFrame.import_csv(file_paths)
        return csv_df

    def merge_terminology(self, file_paths):
        for file_ext in file_paths:
            if file_ext == ".xlsx":
                self.import_xlsx(file_paths)
            if file_ext == ".csv":
                self.import_csv(file_paths)
        terminology_merged = pd.DataFrame.merge_terminology()

    def export_merged_terminology_as_xlsx(self):
        if not self.terminology_merged=True
            terminology_merged = self.terminology_merged.to_excel("./tb_merged.xlsx", index=False)