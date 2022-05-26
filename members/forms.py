from django import forms

class MemberEdit(forms.Form):
    first_name = forms.CharField(label= "名前")
    Mail = forms.EmailField(label="メールアドレス")
    first_name = forms.CharField(label= "パスワード")