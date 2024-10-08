from rest_framework.exceptions import ValidationError
from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken


class CustomBirthdayValidator:
    def validate_birthday(self, value):
        birthday = list(map(int, (self.context["request"].data["birthday"]).split("-")))
        now = timezone.now()
        now_arr = [now.year, now.month, now.day]
        now_arr2 = [now.year - 15, now.month, now.day]
        if birthday > now_arr:
            raise ValidationError(
                {"msg": "유효하지 않은 생일입니다 다시 입력해주세요."}
            )
        elif birthday > now_arr2:
            raise ValidationError({"msg": "15세 이상만 가입할 수 있습니다.."})
        return value


class CustomProfileDeleteValidator:
    def validata_refresh(self, value):
        data = self.context["request"].data
        if not "refresh" in data:
            raise ValidationError({"msg": "refresh_token 값을 입력해주세요."})
        refresh_token = RefreshToken(data["refresh"])
        refresh_token.blacklist()
        return value

    def validate_check_password(self, value):
        user = self.context["request"].user
        if not user.check_password(value):
            raise ValidationError(
                {"msg": "비밀번호가 일치하지 않습니다. 다시 입력해주세요."}
            )
        return value


class CustomPasswordValidator:
    def validate_old_password(self, value):
        user = self.context["request"].user
        if not user.check_password(value):
            raise ValidationError(
                {"msg": "기존 비밀번호가 일치하지 않습니다. 다시 입력해주세요."}
            )
        return value

    def validate(self, data):
        user = self.context["request"].user
        if data["password1"] != data["password2"]:
            raise ValidationError(
                {"msg": "새로운 비밀번호가 일치하지 않습니다. 다시 입력해주세요."}
            )
        if user.check_password(data["password1"]):
            raise ValidationError(
                {"msg": "이전 비밀번호와 동일한 비밀번호입니다. 다시 입력해주세요."}
            )
        return data

    def update(self, instance, validated_data):
        instance.set_password(validated_data["password1"])
        instance.save()
        return instance
