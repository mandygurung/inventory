from django.contrib.auth.mixins import AccessMixin
import xlwt
from django.apps import apps
# class ResponseMixin:

#     def set_cookies(self, response, **kwargs):
#         pass

#     def get_response(self, data, status_code, cookies=False):
#         response = Response(
#             data=data,
#             status=status_code
#         )

#         if cookies:
#             response = self.set_cookies(response)


class JWTTokenRequiredMixins(AccessMixin):

    def dispatch(self, request, *args, **kwargs) :
        if not request.headers.get("Authorization") and not request.COOKIES.get("refresh_token"):
            return self.handle_no_permission()        
        response = super().dispatch(request, *args, **kwargs) # type: ignore

        return response


class ExportToCSVMixin:

    def export_to_csv(self, model, response):
        work_book = xlwt.Workbook(encoding="utf-8")

        sheet =  work_book.add_sheet(model.__name__)

        header_font_style = xlwt.XFStyle()

        header_font_style.font.bold = True

        row_font = xlwt.XFStyle()

        rows = model.objects.values()

        header = True



        for row_index, row in enumerate(rows):
            for num, key in enumerate(row):
                if header:
                    print(header)
                    if num < len(row)-1:
                        sheet.write(0, num, key, header_font_style)
                        sheet.write(1, num, str(row[key]), row_font)
                    else:
                        sheet.write(0, num, key, header_font_style)
                        sheet.write(1, num, str(row[key]), row_font)
                        header = False
                else:
                    sheet.write(row_index+2, num, str(row[key]), row_font)
        work_book.save(response)


