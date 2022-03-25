from django import forms
from .models import Senryu

class SenryuRegist(forms.ModelForm):
    def __init__(self, *args, **kwd):
        super(SenryuRegist, self).__init__(*args, **kwd)

        # 入力必須ではない入力の設定
        self.fields["name"].required = False
        self.fields["comment"].required = False

    class  Meta:
        model = Senryu
        fields = ('name', 'ku1', 'ku2', 'ku3', 'comment')
        labels={
            'name':'雅号',
            'ku1':'初句',
            'ku2':'二句',
            'ku3':'結句',
            'comment':'コメント',
        }

        # エラーメッセージを追加
        error_messages = {
            "ku1": {
                "required": "初句が入力されていません",
            },
            "ku2": {
                "required": "二句が入力されていません",
            },
            "ku3": {
                "required": "結句が入力されていません",
            },
        }

    '''def clean_ku1(self):
        ku1 = self.cleaned_data.get('ku1')
        if len(ku1) < 1:
            raise forms.ValidationError('初句が入力されていません')
        return ku1'''

    '''def clean_ku2(self):
        ku2 = self.cleaned_data['ku2']
        if len(ku2) < 1:
            raise forms.ValidationError('二句が入力されていません')

        return ku2

    def clean_ku3(self):
        ku3= self.cleaned_data['ku3']
        if len(ku3) < 1:
            raise forms.ValidationError('結句が入力されていません')

        return ku3

    def clean(self):
        return self.cleaned_data'''
