```python
# Importieren des Moduls transducers
from transducers import *

"""
Diese Datei enthält Beispielausgaben

Damit alle Ausgaben ausgeführt werden können müssen die Module Pandas und Numpy installiert sein.
"""
```




    '\nDiese Datei enthält Beispielausgaben\n\nDamit alle Ausgaben ausgeführt werden können müssen die Module Pandas und Numpy installiert sein.\n'



# 1. Das regelmäßige Verb
### a) Paradigma


```python
vg = VerbGenerator("gel")
vg.setFeatures(["1","SG"])
vg.paradigm()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Simple</th>
      <th>Past</th>
      <th>Conditional</th>
      <th>Past &amp; Conditional</th>
      <th>Inferential</th>
      <th>Inferential &amp; Conditional</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Present</th>
      <td>geliyorum</td>
      <td>geliyordum</td>
      <td>geliyorsam</td>
      <td>geliyorduysam</td>
      <td>geliyormuşum</td>
      <td>geliyormuşsam</td>
    </tr>
    <tr>
      <th>Future</th>
      <td>geleceğim</td>
      <td>gelecektim</td>
      <td>geleceksem</td>
      <td>gelecektiysem</td>
      <td>gelecekmişim</td>
      <td>gelecekmişsem</td>
    </tr>
    <tr>
      <th>Aorist</th>
      <td>gelirim</td>
      <td>gelirdim</td>
      <td>gelirsem</td>
      <td>gelirdiysem</td>
      <td>gelirmişim</td>
      <td>gelirmişsem</td>
    </tr>
    <tr>
      <th>miş-past</th>
      <td>gelmişim</td>
      <td>gelmiştim</td>
      <td>gelmişsem</td>
      <td>gelmiş idiysem</td>
      <td>gelmiş imişim</td>
      <td>gelmiş imişsem</td>
    </tr>
    <tr>
      <th>di-past</th>
      <td>geldim</td>
      <td>geldiydim</td>
      <td>geldiysem</td>
      <td>geldi idiysem</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>Conditional</th>
      <td>gelsem</td>
      <td>gelseydim</td>
      <td></td>
      <td></td>
      <td>gelseymişim</td>
      <td></td>
    </tr>
    <tr>
      <th>Optative</th>
      <td>geleyim</td>
      <td>geleydim</td>
      <td></td>
      <td></td>
      <td>geleymişim</td>
      <td></td>
    </tr>
    <tr>
      <th>Necessitative</th>
      <td>gelmeliyim</td>
      <td>gelmeliydim</td>
      <td>gelmeliysem</td>
      <td>gelmeliydiysem</td>
      <td>gelmeliymişim</td>
      <td></td>
    </tr>
  </tbody>
</table>
</div>



### b) Konjugation


```python
vg.conjugate()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>SG</th>
      <th>PL</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>geliyorum</td>
      <td>geliyoruz</td>
    </tr>
    <tr>
      <th>2</th>
      <td>geliyorsun</td>
      <td>geliyorsunuz</td>
    </tr>
    <tr>
      <th>3</th>
      <td>geliyor</td>
      <td>geliyorlar</td>
    </tr>
  </tbody>
</table>
</div>



### c) Analyse


```python
vg.analyze()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Lexical</th>
      <td>gel</td>
      <td>PRES</td>
      <td>1SG</td>
    </tr>
    <tr>
      <th>Intermediate</th>
      <td>gel</td>
      <td>&lt;Iyor</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Surface</th>
      <td>gel</td>
      <td>iyor</td>
      <td>um</td>
    </tr>
  </tbody>
</table>
</div>



## Interrogativ
### a) Paradigma


```python
vg = VerbGenerator("ye")
vg.setPerson("1")
vg.setFeatures(["1","SG","INT"])
vg.paradigm()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Simple</th>
      <th>Past</th>
      <th>Conditional</th>
      <th>Past &amp; Conditional</th>
      <th>Inferential</th>
      <th>Inferential &amp; Conditional</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Present</th>
      <td>yiyor muyum</td>
      <td>yiyor muydum</td>
      <td>yiyor muysam</td>
      <td>yiyor muyduysam</td>
      <td>yiyor muymuşum</td>
      <td>yiyor muymuşsam</td>
    </tr>
    <tr>
      <th>Future</th>
      <td>yiyecek miyim</td>
      <td>yiyecek miydim</td>
      <td>yiyecek miysem</td>
      <td>yiyecek miydiysem</td>
      <td>yiyecek miymişim</td>
      <td>yiyecek miymişsem</td>
    </tr>
    <tr>
      <th>Aorist</th>
      <td>yer miyim</td>
      <td>yer miydim</td>
      <td>yer miysem</td>
      <td>yer miydiysem</td>
      <td>yer miymişim</td>
      <td>yer miymişsem</td>
    </tr>
    <tr>
      <th>miş-past</th>
      <td>yemiş miyim</td>
      <td>yemiş miydim</td>
      <td>yemiş miysem</td>
      <td>yemiş miydiysem</td>
      <td>yemiş miymişim</td>
      <td>yemiş miymişsem</td>
    </tr>
    <tr>
      <th>di-past</th>
      <td>yedim mi</td>
      <td>yedim miydi</td>
      <td>yedim miyse</td>
      <td>yedim miydiyse</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>Conditional</th>
      <td>yesem mi</td>
      <td>yesem miydi</td>
      <td></td>
      <td></td>
      <td>yesem miymiş</td>
      <td></td>
    </tr>
    <tr>
      <th>Optative</th>
      <td>yiyeyim mi</td>
      <td>yiyeyim miydi</td>
      <td></td>
      <td></td>
      <td>yiyeyim miymiş</td>
      <td></td>
    </tr>
    <tr>
      <th>Necessitative</th>
      <td>yemeli miyim</td>
      <td>yemeli miydim</td>
      <td>yemeli miysem</td>
      <td>yemeli miydiysem</td>
      <td>yemeli miymişim</td>
      <td></td>
    </tr>
  </tbody>
</table>
</div>



### b) Konjugation


```python
vg.conjugate()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>SG</th>
      <th>PL</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>yiyor muyum</td>
      <td>yiyor muyuz</td>
    </tr>
    <tr>
      <th>2</th>
      <td>yiyor musun</td>
      <td>yiyor musunuz</td>
    </tr>
    <tr>
      <th>3</th>
      <td>yiyor mu</td>
      <td>yiyorlar mı</td>
    </tr>
  </tbody>
</table>
</div>



### c) Analyse


```python
vg.analyze()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Lexical</th>
      <td>ye</td>
      <td>PRES</td>
      <td>INT</td>
      <td>1SG</td>
    </tr>
    <tr>
      <th>Intermediate</th>
      <td>ye</td>
      <td>&lt;Iyor</td>
      <td>#mI</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Surface</th>
      <td>y</td>
      <td>iyor</td>
      <td>mu</td>
      <td>yum</td>
    </tr>
  </tbody>
</table>
</div>



## Negation
### a) Paradigma


```python
vg = VerbGenerator("gel")
vg.setPerson("1")
vg.setFeatures(["1","SG","NEG"])
vg.paradigm()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Simple</th>
      <th>Past</th>
      <th>Conditional</th>
      <th>Past &amp; Conditional</th>
      <th>Inferential</th>
      <th>Inferential &amp; Conditional</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Present</th>
      <td>gelmiyorum</td>
      <td>gelmiyordum</td>
      <td>gelmiyorsam</td>
      <td>gelmiyorduysam</td>
      <td>gelmiyormuşum</td>
      <td>gelmiyormuşsam</td>
    </tr>
    <tr>
      <th>Future</th>
      <td>gelmeyeceğim</td>
      <td>gelmeyecektim</td>
      <td>gelmeyeceksem</td>
      <td>gelmeyecektiysem</td>
      <td>gelmeyecekmişim</td>
      <td>gelmeyecekmişsem</td>
    </tr>
    <tr>
      <th>Aorist</th>
      <td>gelmem</td>
      <td>gelmezdim</td>
      <td>gelmezsem</td>
      <td>gelmezdiysem</td>
      <td>gelmezmişim</td>
      <td>gelmezmişsem</td>
    </tr>
    <tr>
      <th>miş-past</th>
      <td>gelmemişim</td>
      <td>gelmemiştim</td>
      <td>gelmemişsem</td>
      <td>gelmemiş idiysem</td>
      <td>gelmemiş imişim</td>
      <td>gelmemiş imişsem</td>
    </tr>
    <tr>
      <th>di-past</th>
      <td>gelmedim</td>
      <td>gelmediydim</td>
      <td>gelmediysem</td>
      <td>gelmedi idiysem</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>Conditional</th>
      <td>gelmesem</td>
      <td>gelmeseydim</td>
      <td></td>
      <td></td>
      <td>gelmeseymişim</td>
      <td></td>
    </tr>
    <tr>
      <th>Optative</th>
      <td>gelmeyeyim</td>
      <td>gelmeyeydim</td>
      <td></td>
      <td></td>
      <td>gelmeyeymişim</td>
      <td></td>
    </tr>
    <tr>
      <th>Necessitative</th>
      <td>gelmemeliyim</td>
      <td>gelmemeliydim</td>
      <td>gelmemeliysem</td>
      <td>gelmemeliydiysem</td>
      <td>gelmemeliymişim</td>
      <td></td>
    </tr>
  </tbody>
</table>
</div>



### b) Konjugation


```python
vg = VerbGenerator("gel")
vg.setFeatures(["AOR","NEG"])
vg.conjugate()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>SG</th>
      <th>PL</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>gelmem</td>
      <td>gelmeyiz</td>
    </tr>
    <tr>
      <th>2</th>
      <td>gelmezsin</td>
      <td>gelmezsiniz</td>
    </tr>
    <tr>
      <th>3</th>
      <td>gelmez</td>
      <td>gelmezler</td>
    </tr>
  </tbody>
</table>
</div>



### c) Analyse


```python
vg.analyze()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Lexical</th>
      <td>gel</td>
      <td>NEG</td>
      <td>AOR</td>
      <td>3SG</td>
    </tr>
    <tr>
      <th>Intermediate</th>
      <td>gel</td>
      <td>M</td>
      <td>R</td>
      <td>@</td>
    </tr>
    <tr>
      <th>Surface</th>
      <td>gel</td>
      <td>mez</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>
</div>



## Negation + Interrogativ
### a) Paradigma


```python
vg = VerbGenerator("gel")
vg.setFeatures(["1","SG","INT","NEG"])
vg.paradigm()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Simple</th>
      <th>Past</th>
      <th>Conditional</th>
      <th>Past &amp; Conditional</th>
      <th>Inferential</th>
      <th>Inferential &amp; Conditional</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Present</th>
      <td>gelmiyor muyum</td>
      <td>gelmiyor muydum</td>
      <td>gelmiyor muysam</td>
      <td>gelmiyor muyduysam</td>
      <td>gelmiyor muymuşum</td>
      <td>gelmiyor muymuşsam</td>
    </tr>
    <tr>
      <th>Future</th>
      <td>gelmeyecek miyim</td>
      <td>gelmeyecek miydim</td>
      <td>gelmeyecek miysem</td>
      <td>gelmeyecek miydiysem</td>
      <td>gelmeyecek miymişim</td>
      <td>gelmeyecek miymişsem</td>
    </tr>
    <tr>
      <th>Aorist</th>
      <td>gelmez miyim</td>
      <td>gelmez miydim</td>
      <td>gelmez miysem</td>
      <td>gelmez miydiysem</td>
      <td>gelmez miymişim</td>
      <td>gelmez miymişsem</td>
    </tr>
    <tr>
      <th>miş-past</th>
      <td>gelmemiş miyim</td>
      <td>gelmemiş miydim</td>
      <td>gelmemiş miysem</td>
      <td>gelmemiş miydiysem</td>
      <td>gelmemiş miymişim</td>
      <td>gelmemiş miymişsem</td>
    </tr>
    <tr>
      <th>di-past</th>
      <td>gelmedim mi</td>
      <td>gelmedim miydi</td>
      <td>gelmedim miyse</td>
      <td>gelmedim miydiyse</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>Conditional</th>
      <td>gelmesem mi</td>
      <td>gelmesem miydi</td>
      <td></td>
      <td></td>
      <td>gelmesem miymiş</td>
      <td></td>
    </tr>
    <tr>
      <th>Optative</th>
      <td>gelmeyeyim mi</td>
      <td>gelmeyeyim miydi</td>
      <td></td>
      <td></td>
      <td>gelmeyeyim miymiş</td>
      <td></td>
    </tr>
    <tr>
      <th>Necessitative</th>
      <td>gelmemeli miyim</td>
      <td>gelmemeli miydim</td>
      <td>gelmemeli miysem</td>
      <td>gelmemeli miydiysem</td>
      <td>gelmemeli miymişim</td>
      <td></td>
    </tr>
  </tbody>
</table>
</div>



### b) Konjugation


```python
vg.conjugate()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>SG</th>
      <th>PL</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>gelmiyor muyum</td>
      <td>gelmiyor muyuz</td>
    </tr>
    <tr>
      <th>2</th>
      <td>gelmiyor musun</td>
      <td>gelmiyor musunuz</td>
    </tr>
    <tr>
      <th>3</th>
      <td>gelmiyor mu</td>
      <td>gelmiyorlar mı</td>
    </tr>
  </tbody>
</table>
</div>



### c) Analyse


```python
vg.analyze()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Lexical</th>
      <td>gel</td>
      <td>NEG</td>
      <td>PRES</td>
      <td>INT</td>
      <td>1SG</td>
    </tr>
    <tr>
      <th>Intermediate</th>
      <td>gel</td>
      <td>M</td>
      <td>&lt;Iyor</td>
      <td>#mI</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Surface</th>
      <td>gel</td>
      <td>m</td>
      <td>iyor</td>
      <td>mu</td>
      <td>yum</td>
    </tr>
  </tbody>
</table>
</div>



# 2. Das Verb "sein"
### a) Paradigma


```python
vg = VerbGenerator("yumuşak")
vg.setFeatures(["1","SG","toBE"])
vg.paradigm()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Simple</th>
      <th>Past</th>
      <th>Conditional</th>
      <th>Past &amp; Conditional</th>
      <th>Inferential</th>
      <th>Inferential &amp; Conditional</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>to be</th>
      <td>yumuşağım</td>
      <td>yumuşaktım</td>
      <td>yumuşaksam</td>
      <td>yumuşaktıysam</td>
      <td>yumuşakmışım</td>
      <td>yumuşakmışsam</td>
    </tr>
  </tbody>
</table>
</div>



### b) Konjugation


```python
vg.conjugate()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>SG</th>
      <th>PL</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>yumuşağım</td>
      <td>yumuşağız</td>
    </tr>
    <tr>
      <th>2</th>
      <td>yumuşaksın</td>
      <td>yumuşaksınız</td>
    </tr>
    <tr>
      <th>3</th>
      <td>yumuşak</td>
      <td>yumuşaklar</td>
    </tr>
  </tbody>
</table>
</div>



### c) Analyse


```python
vg.analyze()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Lexical</th>
      <td>yumuşaK</td>
      <td>toBE</td>
      <td>1SG</td>
    </tr>
    <tr>
      <th>Intermediate</th>
      <td>yumuşaK</td>
      <td>@</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Surface</th>
      <td>yumuşağ</td>
      <td></td>
      <td>ım</td>
    </tr>
  </tbody>
</table>
</div>



## Interrogativ
### a) Paradigma


```python
vg = VerbGenerator("hazır")
vg.setFeatures(["1","SG","toBE","INT"])
vg.paradigm()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Simple</th>
      <th>Past</th>
      <th>Conditional</th>
      <th>Past &amp; Conditional</th>
      <th>Inferential</th>
      <th>Inferential &amp; Conditional</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>to be</th>
      <td>hazır mıyım</td>
      <td>hazır mıydım</td>
      <td>hazır mıysam</td>
      <td>hazır mıydıysam</td>
      <td>hazır mıymışım</td>
      <td>hazır mıymışsam</td>
    </tr>
  </tbody>
</table>
</div>



### b) Konjugation


```python
vg.conjugate()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>SG</th>
      <th>PL</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>hazır mıyım</td>
      <td>hazır mıyız</td>
    </tr>
    <tr>
      <th>2</th>
      <td>hazır mısın</td>
      <td>hazır mısınız</td>
    </tr>
    <tr>
      <th>3</th>
      <td>hazır mı</td>
      <td>hazırlar mı</td>
    </tr>
  </tbody>
</table>
</div>



### c) Analyse


```python
vg.analyze()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Lexical</th>
      <td>hazır</td>
      <td>toBE</td>
      <td>INT</td>
      <td>1SG</td>
    </tr>
    <tr>
      <th>Intermediate</th>
      <td>hazır</td>
      <td>@</td>
      <td>#mI</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Surface</th>
      <td>hazır</td>
      <td></td>
      <td>mı</td>
      <td>yım</td>
    </tr>
  </tbody>
</table>
</div>



## Negation
### a) Paradigma


```python
vg = VerbGenerator("hazır")
vg.setFeatures(["1","SG","toBE","NEG"])
vg.paradigm()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Simple</th>
      <th>Past</th>
      <th>Conditional</th>
      <th>Past &amp; Conditional</th>
      <th>Inferential</th>
      <th>Inferential &amp; Conditional</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>to be</th>
      <td>hazır değilim</td>
      <td>hazır değildim</td>
      <td>hazır değilsem</td>
      <td>hazır değildiysem</td>
      <td>hazır değilmişim</td>
      <td>hazır değilmişsem</td>
    </tr>
  </tbody>
</table>
</div>



## b) Konjugation


```python
vg.conjugate()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>SG</th>
      <th>PL</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>hazır değilim</td>
      <td>hazır değiliz</td>
    </tr>
    <tr>
      <th>2</th>
      <td>hazır değilsin</td>
      <td>hazır değilsiniz</td>
    </tr>
    <tr>
      <th>3</th>
      <td>hazır değil</td>
      <td>hazır değiller</td>
    </tr>
  </tbody>
</table>
</div>



### c) Analyse


```python
vg.analyze()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Lexical</th>
      <td>hazır</td>
      <td>NEG</td>
      <td>toBE</td>
      <td>1SG</td>
    </tr>
    <tr>
      <th>Intermediate</th>
      <td>hazır</td>
      <td>M</td>
      <td>@</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Surface</th>
      <td>hazır</td>
      <td>değil</td>
      <td></td>
      <td>im</td>
    </tr>
  </tbody>
</table>
</div>



## Negation + Interrogativ
### a) Paradigma


```python
vg = VerbGenerator("hazır")
vg.setFeatures(["1","SG","toBE","NEG","INT"])
vg.setInterrogative()
vg.paradigm()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Simple</th>
      <th>Past</th>
      <th>Conditional</th>
      <th>Past &amp; Conditional</th>
      <th>Inferential</th>
      <th>Inferential &amp; Conditional</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>to be</th>
      <td>hazır değil miyim</td>
      <td>hazır değil miydim</td>
      <td>hazır değil miysem</td>
      <td>hazır değil miydiysem</td>
      <td>hazır değil miymişim</td>
      <td>hazır değil miymişsem</td>
    </tr>
  </tbody>
</table>
</div>



### b) Konjugation


```python
vg.conjugate()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>SG</th>
      <th>PL</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>hazır değil miyim</td>
      <td>hazır değil miyiz</td>
    </tr>
    <tr>
      <th>2</th>
      <td>hazır değil misin</td>
      <td>hazır değil misiniz</td>
    </tr>
    <tr>
      <th>3</th>
      <td>hazır değil mi</td>
      <td>hazır değiller mi</td>
    </tr>
  </tbody>
</table>
</div>



### c) Analyse


```python
vg.analyze()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Lexical</th>
      <td>hazır</td>
      <td>NEG</td>
      <td>toBE</td>
      <td>INT</td>
      <td>1SG</td>
    </tr>
    <tr>
      <th>Intermediate</th>
      <td>hazır</td>
      <td>M</td>
      <td>@</td>
      <td>#mI</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Surface</th>
      <td>hazır</td>
      <td>değil</td>
      <td></td>
      <td>mi</td>
      <td>yim</td>
    </tr>
  </tbody>
</table>
</div>



# 3. Partizipien
- Beispiel: yaşamak (leben); Präsens


```python
vg = VerbGenerator("yaşa")
vg.setBase("PRES")
vg.setParticiple()
vg.form()
```




    'yaşayan'



# 4. Komplexe Formen
## Zusammengesetzte Formen + Verbstammerweiterung

### yapabileceksek: 
- yap + ['PL', '1', 'FUTURE', 'CONDfeature', 'POT']
- Features werden hier durch einzelne Funktionen gesetzt


```python
# Instanziierung mit Verbstamm
vg = VerbGenerator("yap")
# Verbbasis bestimmen
vg.setBase("FUTURE")
# Person bestimmen
vg.setPerson("1")
# Numerus bestimmen
vg.setNumber("PL")
# Potentialis-Feature
vg.setPotential()
# Conditional-Ergänzung
vg.setConditional()
# Form ausgeben
vg.form()
```




    'yapabileceksek'




```python
# Analyse ausgeben
vg.analyze()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Lexical</th>
      <td>yap</td>
      <td>POT</td>
      <td>FUTURE</td>
      <td>CONDfeature</td>
      <td>1PL</td>
    </tr>
    <tr>
      <th>Intermediate</th>
      <td>yap</td>
      <td>YEbil</td>
      <td>YEcEK</td>
      <td>!sE</td>
      <td>k</td>
    </tr>
    <tr>
      <th>Surface</th>
      <td>yap</td>
      <td>abil</td>
      <td>ecek</td>
      <td>se</td>
      <td>k</td>
    </tr>
  </tbody>
</table>
</div>



### dayanıştırtılamayabilecek miymişiz: 
- dayan + ['RECIP', 'CAUS2', 'PASS', 'IMPOT', 'POT', 'FUTURE', 'INT', 'INFER', '1', 'PL']


```python
# Initialisierung
vg = VerbGenerator("dayan")
# Featureliste übergeben
vg.setFeatures(['RECIP', 'CAUS', 'PASS', 'IMPOT', 'POT', 
                'FUTURE', 'INT', 'INFER', '1', 'PL'])
# Form ausgeben
vg.analyze()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>8</th>
      <th>9</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Lexical</th>
      <td>dayan</td>
      <td>RECIP</td>
      <td>CAUS</td>
      <td>PASS</td>
      <td>IMPOT</td>
      <td>POT</td>
      <td>FUTURE</td>
      <td>INT</td>
      <td>INFER</td>
      <td>1PL</td>
    </tr>
    <tr>
      <th>Intermediate</th>
      <td>dayan</td>
      <td>Ş</td>
      <td>C</td>
      <td>L</td>
      <td>YEM</td>
      <td>YEbil</td>
      <td>YEcEK</td>
      <td>#mI</td>
      <td>?mIş</td>
      <td>YIz</td>
    </tr>
    <tr>
      <th>Surface</th>
      <td>dayan</td>
      <td>ış</td>
      <td>tır</td>
      <td>ıl</td>
      <td>ama</td>
      <td>yabil</td>
      <td>ecek</td>
      <td>mi</td>
      <td>ymiş</td>
      <td>iz</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Analyse ausgeben
vg.form()
```




    'dayanıştırılamayabilecek miymişiz'



### yıkandırtılmamışsam:
- yıka + ['REFL', 'CAUS2', 'PASS', 'NEG', 'CONDfeature', 'MIS', '1', 'SG']


```python
# Initialisierung
vg = VerbGenerator("yıka")
# Featureliste übergeben
vg.setFeatures(['REFL', 'CAUS2', 'PASS', 'NEG', 'CONDfeature', 'MIS', '1', 'SG'])
# Form ausgeben
vg.analyze()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>8</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Lexical</th>
      <td>yıka</td>
      <td>REFL</td>
      <td>CAUS</td>
      <td>CAUS</td>
      <td>PASS</td>
      <td>NEG</td>
      <td>MIS</td>
      <td>CONDfeature</td>
      <td>1SG</td>
    </tr>
    <tr>
      <th>Intermediate</th>
      <td>yıka</td>
      <td>N</td>
      <td>C</td>
      <td>C</td>
      <td>L</td>
      <td>M</td>
      <td>mIş</td>
      <td>!sE</td>
      <td>m</td>
    </tr>
    <tr>
      <th>Surface</th>
      <td>yıka</td>
      <td>n</td>
      <td>dır</td>
      <td>t</td>
      <td>ıl</td>
      <td>ma</td>
      <td>mış</td>
      <td>sa</td>
      <td>m</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Analyse ausgeben
vg.form()
```




    'yıkandırtılmamışsam'



# 5. Unregelmäßige Verben
## Die unregelmäßigen Stämme ye und de


```python
vg = VerbGenerator("ye")
vg.setFeatures(["2","PL","PRES"])
print(vg.form())
vg = VerbGenerator("de")
vg.setFeatures(["1","PL","DI"])
print(vg.form())
```

    yiyorsunuz
    dedik
    

## Unregelmäßige Stämme des Aorist


```python
# regelmäßiger Stamm "yap" mit "-Er"
vg = VerbGenerator("yap")
vg.setFeatures(["1","SG","AOR"])
print(vg.form())
# unregelmäßiger Stamm "ol" mit "-Ir"
vg = VerbGenerator("ol")
vg.setFeatures(["1","SG","AOR"])
print(vg.form())
```

    yaparım
    olurum
    

## Konsonantenassimilation
### Stämme: git, tat, et


```python
# unregelmäßiger Stamm "git"
vg = VerbGenerator("git")
vg.setFeatures(["1","PL","FUTURE"])
print(vg.form())
# unregelmäßiger Stamm "et" als Hilfsverb
vg = VerbGenerator("yardım et")
vg.setFeatures(["1","SG","OPT","INT"])
print(vg.form())
```

    gideceğiz
    yardım edeyim mi
    

# 6. Vergleich mit handannotierten Formen
- In der Datei tagged_words.txt befinden sich 67 handannotierte Verbformen, die mit dem entsprechenden Verbstamm und den Features annotiert sind.
- Zur Evaluierung werden diese Formen anhand der Annotationen neu generiert und mit den Originalformen verglichen
- Eine Übersicht verschafft die anschließend ausgegebene Liste


```python
# Datei verarbeiten und eine Liste der annotierten Wörter erstellen
aw = open("annotated_words.txt",encoding="UTF-8")
aw_read = aw.read()
annotatedWords = [[element.split("\t")[0],element.split("\t")[1].split("|")] for element in aw_read.split("\n") if element != ""]
aw.close()

# Variablen zuweisen
# Liste für die ausgabe
evaluated_words = []
# Index des Wortes für die Übersicht der Ausgabeliste
num = 0
# Anzahl der richtig generierten Formen
correct = 0
# Anzahl der falsch generierten Formen
wrong = 0
# Liste für die ausgabe erstellen
for annotatedWord in annotatedWords:
    num += 1
    stem,featureList,gold_form = annotatedWord[1][0],annotatedWord[1][1:],annotatedWord[0]
    # Form generieren
    vg = VerbGenerator(stem)
    vg.setFeatures(featureList)
    generated_form = vg.form()
    # Als richtig oder falsch einstufen
    if generated_form == gold_form:
        match = "correct"
        correct += 1
    else:
        match = "wrong"
        wrong += 1
    # Listenintrag erstellen
    evaluated_words += [[str(num),gold_form,stem," ".join(featureList),match]]

# Alle Einträge formatiert in Tabelle ausgeben
for word in evaluated_words:
    if len(word) == 5:
        print("{:5} {:40} {:10} {:50} {:20}".format(word[0],word[1],word[2],word[3],word[4]))
print()
# Anzahl richtig und falsch generierter Wörter
print("correct forms generated: "+str(correct)+" of "+str(len(annotatedWords)))
print("wrong forms generated: "+str(wrong)+" of "+str(len(annotatedWords)))
```

    1     geliyorum                                gel        PRES 1 SG                                          correct             
    2     geliyordum                               gel        PRES PAST 1 SG                                     correct             
    3     geliyorsam                               gel        PRES CONDfeature 1 SG                              correct             
    4     geliyorduysam                            gel        PRES PAST CONDfeature 1 SG                         correct             
    5     geliyormuşum                             gel        PRES INFER 1 SG                                    correct             
    6     geliyormuşsam                            gel        PRES INFER CONDfeature 1 SG                        correct             
    7     geleceğim                                gel        FUTURE 1 SG                                        correct             
    8     gelecektim                               gel        FUTURE PAST 1 SG                                   correct             
    9     geleceksem                               gel        FUTURE CONDfeature 1 SG                            correct             
    10    gelecektiysem                            gel        FUTURE PAST CONDfeature 1 SG                       correct             
    11    gelecekmişim                             gel        FUTURE INFER 1 SG                                  correct             
    12    gelecekmişsem                            gel        FUTURE INFER CONDfeature 1 SG                      correct             
    13    gelirim                                  gel        AOR 1 SG                                           correct             
    14    gelirdim                                 gel        AOR PAST 1 SG                                      correct             
    15    gelirsem                                 gel        AOR CONDfeature 1 SG                               correct             
    16    gelirdiysem                              gel        AOR PAST CONDfeature 1 SG                          correct             
    17    gelirmişim                               gel        AOR INFER 1 SG                                     correct             
    18    gelirmişsem                              gel        AOR INFER CONDfeature 1 SG                         correct             
    19    gelmişim                                 gel        MIS 1 SG                                           correct             
    20    gelmiştim                                gel        MIS PAST 1 SG                                      correct             
    21    gelmişsem                                gel        MIS CONDfeature 1 SG                               correct             
    22    gelmiş idiysem                           gel        MIS PAST CONDfeature 1 SG                          correct             
    23    gelmiş imişim                            gel        MIS INFER 1 SG                                     correct             
    24    gelmiş imişsem                           gel        MIS INFER CONDfeature 1 SG                         correct             
    25    geldim                                   gel        DI 1 SG                                            correct             
    26    geldiydim                                gel        DI PAST 1 SG                                       correct             
    27    geldiysem                                gel        DI CONDfeature 1 SG                                correct             
    28    geldi idiysem                            gel        DI PAST CONDfeature 1 SG                           correct             
    29    gelsem                                   gel        COND 1 SG                                          correct             
    30    gelseydim                                gel        COND PAST 1 SG                                     correct             
    31    gelseymişim                              gel        COND INFER 1 SG                                    correct             
    32    geleyim                                  gel        OPT 1 SG                                           correct             
    33    geleydim                                 gel        OPT PAST 1 SG                                      correct             
    34    geleymişim                               gel        OPT INFER 1 SG                                     correct             
    35    gelmeliyim                               gel        NEC 1 SG                                           correct             
    36    gelmeliydim                              gel        NEC PAST 1 SG                                      correct             
    37    gelmeliysem                              gel        NEC CONDfeature 1 SG                               correct             
    38    gelmeliydiysem                           gel        NEC PAST CONDfeature 1 SG                          correct             
    39    gelmeliymişim                            gel        NEC INFER 1 SG                                     correct             
    40    yapabileceksek                           yap        POT FUTURE CONDfeature 1 PL                        correct             
    41    gelmedi                                  gel        NEG DI 3 SG                                        correct             
    42    gelmez                                   gel        NEG AOR 3 SG                                       correct             
    43    gelebilirim                              gel        POT AOR 1 SG                                       correct             
    44    gelemedi                                 gel        IMPOT DI 3 SG                                      correct             
    45    gelmeyebilirim                           gel        NEG POT AOR 1 SG                                   correct             
    46    gelemeyebilirim                          gel        IMPOT POT AOR 1 SG                                 correct             
    47    gelmezsin                                gel        NEG AOR 2 SG                                       correct             
    48    alıyor musun                             al         INT PRES 2 SG                                      correct             
    49    yaptınız mı                              yap        INT DI 2 PL                                        correct             
    50    alıyor muydun                            al         INT PRES PAST 2 SG                                 correct             
    51    geldiniz miydi                           gel        INT DI PAST 2 PL                                   correct             
    52    evdeyim                                  evde       toBE 1 SG                                          correct             
    53    evdeydim                                 evde       toBE PAST 1 SG                                     correct             
    54    evdeysem                                 evde       toBE CONDfeature 1 SG                              correct             
    55    evdeydiysem                              evde       toBE PAST CONDfeature 1 SG                         correct             
    56    evdeydiymişim                            evde       toBE PAST INFER 1 SG                               correct             
    57    evdeymişim                               evde       toBE INFER 1 SG                                    correct             
    58    evdeymişsem                              evde       toBE CONDfeature INFER 1 SG                        correct             
    59    evde değilim                             evde       toBE NEG 1 SG                                      correct             
    60    evde miyim                               evde       toBE INT 1 SG                                      correct             
    61    evde miydim                              evde       toBE INT PAST 1 SG                                 correct             
    62    dayanıştırılamayabilecek miymişiz        dayan      RECIP CAUS PASS IMPOT POT FUTURE INT INFER 1 PL    correct             
    63    bekleyecek                               bekle      FUTURE 3 SG                                        correct             
    64    yıkandırtılmamışsam                      yıka       REFL CAUS2 PASS NEG CONDfeature MIS 1 SG           correct             
    65    tamir ediyorlar                          tamir et   PRES 3 PL                                          correct             
    66    diyelim                                  de         OPT 1 PL                                           correct             
    67    yiyeceğiz                                ye         FUTURE 1 PL                                        correct             
    68    gelen                                    gel        PRES PART                                          correct             
    69    geldik                                   gel        DI PART                                            correct             
    
    correct forms generated: 69 of 69
    wrong forms generated: 0 of 69
    


```python

```
