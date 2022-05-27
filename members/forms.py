from django import forms
from .models import Members
import re
import hashlib
from pprint import pprint

class MemberRegist(forms.Form):
    name = forms.CharField(label = "名前"
        , max_length=30
    )
    email = forms.EmailField(label ="メールアドレス"
        , max_length=100
    )
    email2 = forms.EmailField(label ="メールアドレス(確認用)"
        , max_length=100
    )
    password = forms.CharField(label= "パスワード"
        , widget=forms.PasswordInput()
        , min_length=8
        , max_length=100
        , required=True
    )
    password2 = forms.CharField(label = "パスワード(確認用)"
        , widget=forms.PasswordInput()
        , min_length=8
        , max_length=100
        , required=True
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        cnt = Members.objects.filter(status = 1, email = email).count()
        print(cnt)
        if cnt > 0:
            raise forms.ValidationError("既に登録済みのメールアドレスです")
        return email

    def clean_password(self):
        password = self.cleaned_data['password']
        if not re.search(r'\d', password) or not re.search(r'[a-zA-Z]', password):
            raise forms.ValidationError("英字と数字を入力し下さい")
        return password

    '''def clean_password2(self):
        password2 = self.cleaned_data('password2')
        return password2'''
 
    def clean(self):
        cleaned_data = super().clean()

        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            self.add_error('password', 'パスワード(確認用)と一致しません')

        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            self.add_error('email', 'メールアドレス(確認用)と一致しません')
        return cleaned_data

class MemberLogin(forms.Form):
    email = forms.EmailField(label = "メールアドレス"
        , max_length=100
    )
    password = forms.CharField(label= "パスワード"
        , widget=forms.PasswordInput()
        , min_length=8
        , max_length=100
        , required=True
    )

    def clean(self):
        cleaned_data = super().clean()
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        if email and password:
            password = hashlib.sha256(password.encode()).hexdigest()
            rec = Members.objects.filter(email = email, status = 1)
            if len(rec) != 1 or password != rec[0].password:
                raise forms.ValidationError("入力に間違いがあります")
        return cleaned_data

class MemberPassword(forms.Form):
    password0 = forms.CharField(label= "現在のパスワード"
        , widget=forms.PasswordInput()
        , min_length=8
        , max_length=100
        , required=True
    )

    password = forms.CharField(label= "パスワード"
        , widget=forms.PasswordInput()
        , min_length=8
        , max_length=100
        , required=True
    )

    password2 = forms.CharField(label = "パスワード(確認用)"
        , widget=forms.PasswordInput()
        , min_length=8
        , max_length=100
        , required=True
    )
    def clean_password(self):
        password = self.cleaned_data['password']
        if not re.search(r'\d', password) or not re.search(r'[a-zA-Z]', password):
            raise forms.ValidationError("英字と数字を入力し下さい")
        return password

    def clean(self):
        cleaned_data = super().clean()
        password0 = self.cleaned_data.get('password0')
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password0 and password and password2:
            if password != password2:
                self.add_error('password', 'パスワード(確認用)と一致しません')

            password = hashlib.sha256(password.encode()).hexdigest()
            password0 = hashlib.sha256(password0.encode()).hexdigest()
            rec = Members.objects.filter(password = password0, status = 1)
            pprint(vars(rec))
            if password == rec[0].password:
                self.add_error('password', '現在のパスワードと同じパスワードは設定できません')

        return cleaned_data

class MemberEmail(forms.Form):
    email = forms.EmailField(label ="メールアドレス"
        , max_length=100
    )
    email2 = forms.EmailField(label ="メールアドレス(確認用)"
        , max_length=100
    )
    def clean_email(self):
        email = self.cleaned_data.get('email')
        cnt = Members.objects.filter(email = email, status = 1).count()
        print(cnt)
        if cnt > 0:
            raise forms.ValidationError("既に登録済みのメールアドレスです")
        return email

    def clean(self):
        cleaned_data = super().clean()
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email and email2:
            if email != email2:
                self.add_error('password', 'メールアドレス(確認用)と一致しません')

        return cleaned_data