#import zfile as zipfile
importar arquivo zip
#from zipfile import ZipFile

def all (_in, _out, dp = None):
    se dp:
        retornar allWithProgress (_in, _out, dp)
    retornar allNoProgress (_in, _out)

def allNoProgress (_in, _out):
    experimentar:
        zin = zipfile.ZipFile (_in, 'r')
        zin.extractall (_out)
    exceto exceção como e:
        imprimir (str (e))
        retorna falso
    retornar verdadeiro

def allWithProgress (_in, _out, dp):
    zin = zipfile.ZipFile (_in, 'r')
    nFiles = float (len (zin.infolist ()))
    contagem = 0
    experimentar:
        para item em zin.infolist ():
            contagem + = 1
            update = count / nFiles * 100
            dp.update (int (atualização))
            zin.extract (item, _out)
    exceto exceção como e:
        imprimir (str (e))
        retorna falso

    retornar verdadeiro
#checkintegrity30122019
