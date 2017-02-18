import requests
import xmltodict
from django import forms

class CalcularFreteForm(forms.Form):

    cep = forms.CharField(max_length=9)
    valor_frete = forms.CharField(required=False)

    def calcular_frete(self):
        cep = self.cleaned_data.get('cep')
        r = requests.get('http://ws.correios.com.br/calculador/CalcPrecoPrazo.asmx/CalcPrecoPrazo', params={
            'nCdEmpresa': '',
            'sDsSenha': '',
            'nCdServico': '40010, 41106',
            'sCepOrigem': '04141050',
            'sCepDestino': cep,
            'nVlPeso': '0.200',
            'nCdFormato': '1',
            'nVlComprimento': '23',
            'nVlAltura': '7',
            'nVlLargura': '15',
            'nVlDiametro': '23',
            'sCdMaoPropria': 'N',
            'nVlValorDeclarado': '0',
            'sCdAvisoRecebimento': 'N',
        })
        frete_result = xmltodict.parse(r.text)
        servicos = frete_result.get('cResultado').get('Servicos').get('cServico')
        return {
            'cep': cep,
            'valor_frete_sedex': servicos[0].get('Valor'),
            'valor_frete_pac': servicos[1].get('Valor'),
        }
