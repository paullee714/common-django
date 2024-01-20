from rest_framework.response import Response
from rest_framework import status


class CommonResponse(Response):
    def __init__(
        self,
        data=None,
        res_status=None,
        message=None,
    ):
        if res_status == status.HTTP_200_OK:
            message = "조회에 성공했습니다." if message is None else message
        elif res_status == status.HTTP_201_CREATED:
            message = "저장에 성공했습니다." if message is None else message
        else:
            message = "에러가 발생했습니다." if message is None else message

        # Define your custom structure
        custom_data = {
            "success": True
            if res_status in [status.HTTP_200_OK, status.HTTP_201_CREATED]
            else False,
            "message": message,
            "data": data,
        }
        super().__init__(
            data=custom_data,
            status=res_status,
        )
