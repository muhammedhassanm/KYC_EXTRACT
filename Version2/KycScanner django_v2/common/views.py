from django.http import JsonResponse
from django.views import View
from common.Modeling_Code import ModelDetect
from common.Modeling_Code import pdf_extractor
import json


class document_uploaded(View):
    def post(self, request):
        if request.method == 'POST':

            my_bytes_value = request.body
            req_json = my_bytes_value.decode('utf8').replace("'", '"')
            req_json = json.loads(req_json)

            document_type = req_json['documentType']
            document_url  = req_json['documentUrl']

            # Uniqudocument_typee_ID = self.request.POST.get('documentType')
            # document_url = self.request.POST.get('documentUrl')

            if document_type == 'AADHAR_FRONT':
                details = ModelDetect.detect_text_adhar_front(document_url)
                return JsonResponse({'status':"success", 'message':"Success", 'documentType':document_type, 'country':'India', 'aadharFront': details, 'aadharBack': None, 'pancard':None})
            if document_type == 'AADHAR_BACK':
                details = ModelDetect.detect_text_adhar_back(document_url)
                return JsonResponse({'status':"success", 'message':"Success", 'documentType':document_type, 'country':'India', 'aadharFront':None, 'aadharBack':details, 'pancard':None})
            if document_type == 'PANCARD':
                details = ModelDetect.detect_text_pan_card(document_url)
                return JsonResponse({'status':"success", 'message':"Success", 'documentType':document_type, 'country':'India', 'aadharFront':None, 'aadharBack':None, 'pancard':details})
            else:
                return JsonResponse({"status": "failed", "message" : "Document Type Not Clear"})

class pdf_uploaded(View):
    def post(self, request):
        if request.method == 'POST':

            my_bytes_value = request.body
            req_json = my_bytes_value.decode('utf8').replace("'", '"')
            req_json = json.loads(req_json)
            pdf_url = req_json['documentUrl']

            try:
                details = pdf_extractor.get_pdf_details(pdf_url)
                for key in details:
                    # type 1
                    if key == 'protect3D':
                        return JsonResponse({'status':"success", 'message':"Success", 'protect3D':details['protect3D'], 'sanchay':None, 'proGrowth':None})
                    # type 3
                    if key == 'proGrowth':
                        return JsonResponse({'status':"success", 'message':"Success", 'proGrowth':details['proGrowth'], 'sanchay':None, 'protect3D':None})
                    # type 4
                    if key == 'sanchay':
                        return JsonResponse({'status':"success", 'message':"Success", 'sanchay':details['sanchay'], 'proGrowth':None, 'protect3D':None})
                    break

            except Exception as e:
                print(e)
                return JsonResponse({"status": "failed", "message" : "Some Error Occured. Please try Again"})