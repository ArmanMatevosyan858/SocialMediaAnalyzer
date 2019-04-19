import xlsxwriter


class FacebookExcel:
    """
	Class to save Instagram API Data to excel
	"""

    def __init__(self):
        self.excel_file_name = 'Facebook.xlsx'
        self.path = '..\\SocialMediaAnalyzer\\output\\'

    def save_to_excel(self, array_id):
        print('this is array ', array_id)
        workbook = xlsxwriter.Workbook(self.path + self.excel_file_name)
        worksheet = workbook.add_worksheet()
        for post_object in array_id:
            for value in post_object.to_excel():
                worksheet.write(array_id.index(post_object), post_object.to_excel().index(value), value)
        workbook.close()
