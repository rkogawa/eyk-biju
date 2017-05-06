import requests
import xmltodict
from django import forms


CODIGO_PAC = '04510'
CODIGO_SEDEX = '04014'

class CalcularFreteForm(forms.Form):

    cep = forms.CharField(max_length=9)
    frete_selecionado = forms.CharField(required=False)

    def calcular_frete(self):
        cep = self.cleaned_data.get('cep')
        r = requests.get('http://ws.correios.com.br/calculador/CalcPrecoPrazo.asmx/CalcPrecoPrazo', params={
            'nCdEmpresa': '',
            'sDsSenha': '',
            'nCdServico': '{}, {}'.format(CODIGO_SEDEX, CODIGO_PAC),
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
        for servico in servicos:
            servico['Descricao'] = 'Sedex' if servico['Codigo'] == str(int(CODIGO_SEDEX)) else 'PAC'
        return {
            'cep': cep,
            'tipo_frete': self.cleaned_data.get('frete_selecionado'),
            'fretes': servicos,
        }
