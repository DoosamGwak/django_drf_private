from rest_framework.exceptions import ValidationError


class CustomProfileDeleteValidator:
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
