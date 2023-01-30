from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None # Bỏ hết mấy cái chú thích đi
            self.fields[fieldname].widget.attrs.update({'class': 'form-control'}) # Thêm lớp boostrap