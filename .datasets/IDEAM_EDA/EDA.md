## Exploración y análisis de series - EDA - Representación gráfica

* Archivo de resultados: D:/R.LTWB/.datasets/IDEAM_EDA/EDA.md
* Fecha y hora de inicio de ejecución: 2022-10-28 08:32:33.546198
* Python versión: 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)]
* Python rutas: ['D:\\R.LTWB\\.src', 'D:\\R.LTWB', 'D:\\R.GISPython', 'D:\\R.HydroTools.wiki', 'D:\\R.TeachingResearchGuide']
* matplotlib versión: 3.6.0
* Print table samples: False
* Start year: 1980
* End year: 2021
* Encuentra este script en https://github.com/rcfdtools/R.LTWB/tree/main/Section03/EDA
* Cláusulas y condiciones de uso en https://github.com/rcfdtools/R.LTWB/blob/main/LICENSE.md
* Créditos: r.cfdtools@gmail.com


### General dataframe information with 514927 IDEAM records

<div align="center">

Datatypes in the dataset

</div>


<div align="center">

|                  | 0              |
|:-----------------|:---------------|
| CodigoEstacion   | object         |
| NombreEstacion   | object         |
| Latitud          | float64        |
| Longitud         | float64        |
| Altitud          | int64          |
| Categoria        | object         |
| Entidad          | object         |
| AreaOperativa    | object         |
| Departamento     | object         |
| Municipio        | object         |
| FechaInstalacion | datetime64[ns] |
| FechaSuspension  | datetime64[ns] |
| IdParametro      | object         |
| Etiqueta         | object         |
| DescripcionSerie | object         |
| Frecuencia       | object         |
| Fecha            | datetime64[ns] |
| Valor            | float64        |
| Grado            | object         |
| Calificador      | object         |
| NivelAprobacion  | object         |

</div>


<div align="center">

Null values in the dataset

</div>


<div align="center">

|                  |      0 |
|:-----------------|-------:|
| CodigoEstacion   |      0 |
| NombreEstacion   |      0 |
| Latitud          |      0 |
| Longitud         |      0 |
| Altitud          |      0 |
| Categoria        |      0 |
| Entidad          |      0 |
| AreaOperativa    |      0 |
| Departamento     |      0 |
| Municipio        |      0 |
| FechaInstalacion |      0 |
| FechaSuspension  | 422201 |
| IdParametro      |      0 |
| Etiqueta         |      0 |
| DescripcionSerie |      0 |
| Frecuencia       |      0 |
| Fecha            |      0 |
| Valor            |      0 |
| Grado            |      0 |
| Calificador      | 506535 |
| NivelAprobacion  |      0 |

</div>


<div align="center">

General statistics table

</div>


<div align="center">

|       |       Latitud |      Longitud |    Altitud |       Valor |
|:------|--------------:|--------------:|-----------:|------------:|
| count | 514927        | 514927        | 514927     | 514927      |
| mean  |     10.0618   |    -73.6262   |    125.831 |     73.8252 |
| std   |      0.612032 |      0.456964 |    159.568 |    433.814  |
| min   |      8.58861  |    -74.39     |      2     |   -176      |
| 25%   |      9.68367  |    -74.1547   |     34     |     22.6    |
| 50%   |     10.1907   |    -73.5934   |     70     |     27.2    |
| 75%   |     10.5664   |    -73.2477   |    170     |     34.8    |
| max   |     10.9986   |    -72.7561   |   1560     |  76114      |

</div>


<div align="center">

Stations in the dataset

</div>


<div align="center">

|     | 0                                               |
|----:|:------------------------------------------------|
|   0 | COLEGIO AGROPECUARIO PAILITAS  - AUT [25025330] |
|   1 | GLORIA LA [23210020]                            |
|   2 | LA GLORIA [23215060]                            |
|   3 | MATA LA [23215050]                              |
|   4 | RAYA LA [25020670]                              |
|   5 | SANTA ISABEL [25021640]                         |
|   6 | TAMALAMEQUE D C [25021590]                      |
|   7 | TAMALAMEQUE [25020090]                          |
|   8 | TERROR EL HACIENDA [25020650]                   |
|   9 | ZAPATOZA [25020660]                             |
|  10 | BELLAVISTA [28040150]                           |
|  11 | CABANA LA HACIENDA [28040360]                   |
|  12 | DESTINO EL [29060150]                           |
|  13 | DONA MARIA [29060560]                           |
|  14 | FUNDACION [29060040]                            |
|  15 | MARIA LA [29060200]                             |
|  16 | MONTERRUBIO [28040100]                          |
|  17 | NUEVA GRANADA [25021630]                        |
|  18 | SAN ANGEL [28040140]                            |
|  19 | SANTA ROSA DE LIMA [29060100]                   |
|  20 | BAYANO [29060350]                               |
|  21 | BONGO EL [29060030]                             |
|  22 | CARMEN EL [29060140]                            |
|  23 | CENIZO EL [29060060]                            |
|  24 | FLORIDA LA [29060190]                           |
|  25 | GAVILAN [29060170]                              |
|  26 | PADELMA [29065020]                              |
|  27 | PALO ALTO [29060270]                            |
|  28 | UNION LA [29060240]                             |
|  29 | ZACAPA [29065010]                               |
|  30 | ESPERANZA LA [29060180]                         |
|  31 | PALMOR EL [29060340]                            |
|  32 | PLAYA LA [29060330]                             |
|  33 | POLY LA [29060220]                              |
|  34 | PRADO SEVILLA [29065030]                        |
|  35 | PROYECTOS LOS [29060250]                        |
|  36 | RUBY EL [29060550]                              |
|  37 | SAN JUAN [29060290]                             |
|  38 | SAN PABLO [29060070]                            |
|  39 | SARA LA [29060230]                              |
|  40 | ENANO EL [29060160]                             |
|  41 | PALMA LA [29060210]                             |
|  42 | SAN ISIDRO [29060280]                           |
|  43 | SEVILLANO [29060310]                            |
|  44 | TASAJERA [29060120]                             |
|  45 | YE LA [15015020]                                |
|  46 | CNO LA RAYA [16060010]                          |
|  47 | HACHARIRA [16070030]                            |
|  48 | ORU [16070040]                                  |
|  49 | PALACIO EL [16050240]                           |
|  50 | PISTA LA [16070020]                             |
|  51 | PUERTO BARCO [16070010]                         |
|  52 | ALGARROBO [28045020]                            |
|  53 | CENTENARIO HACIENDA [28025090]                  |
|  54 | CHIRIGUANA [25025250]                           |
|  55 | GUAIRA LA HACIENDA [28045040]                   |
|  56 | GUAYMARAL [28035040]                            |
|  57 | MOTILONIA CODAZZI [28025070]                    |
|  58 | SOCOMBA [28025080]                              |
|  59 | VILLA ROSA [28035010]                           |
|  60 | AEROPUERTO ALFONSO LOPEZ - [28025502]           |
|  61 | CALLAO EL [28035020]                            |
|  62 | CICOLAC [28015030]                              |
|  63 | GUATAPURI - AUT [28035070]                      |
|  64 | RINCON EL [28025020]                            |
|  65 | SAN JOSE D ORIENTE [28025040]                   |
|  66 | LA PAULINA - AUT [15065040]                     |
|  67 | URUMITA [28015070]                              |
|  68 | AEROPUERTO LAS FLORES [25025090]                |
|  69 | LOS ALAMOS - AUT [25025002]                     |
|  70 | SEIS EL [25025300]                              |
|  71 | ASTREA [25020220]                               |
|  72 | CANAL EL [25020240]                             |
|  73 | CHIMICHAGUA [25021240]                          |
|  74 | CURUMANI D C [25021580]                         |
|  75 | CURUMANI [25020250]                             |
|  76 | POPONTE [25020690]                              |
|  77 | PRIMAVERA LA [25020920]                         |
|  78 | RINCONHONDO [25020260]                          |
|  79 | SALOA [25020270]                                |
|  80 | LA GRAN VIA - AUT [29065130]                    |
|  81 | ALTO DEL ROSARIO [25027400]                     |
|  82 | ARMENIA [25027360]                              |
|  83 | CHAPETONA LA [25027620]                         |
|  84 | LAS AGUADAS [25027490]                          |
|  85 | PALOMAS LAS [25027390]                          |
|  86 | PENONCITO [25027330]                            |
|  87 | REGIDOR [25027410]                              |
|  88 | SAN ROQUE [25027320]                            |
|  89 | VICTORIA LA [25027420]                          |
|  90 | RIO NUEVO [25027630]                            |
|  91 | ARIGUANI HACIENDA - AUT [28017120]              |
|  92 | CAIMANCITO [25027590]                           |
|  93 | CHEMESQUEMENA [28017150]                        |
|  94 | FLORES LAS [28027030]                           |
|  95 | GRACIAS A DIOS HACIENDA [25027080]              |
|  96 | MATILDE LA [28027020]                           |
|  97 | MINA LA [28017110]                              |
|  98 | PUENTE CARRETERA [25027890]                     |
|  99 | REPOSO EL [28017050]                            |
| 100 | SANTA TERESA [28027040]                         |
| 101 | BECERRIL [28027050]                             |
| 102 | CANTACLARO [28037060]                           |
| 103 | CONVENCION HACIENDA [28037020]                  |
| 104 | ISLANDIA [28027160]                             |
| 105 | MARIANGOLA [28037040]                           |
| 106 | PUEBLO BELLO [28047020]                         |
| 107 | PUENTE CALLAO [28037010]                        |
| 108 | PUENTE CANOAS  - AUT [28037090]                 |
| 109 | PUENTE CARRETERA [28037130]                     |
| 110 | PUENTE SALGUERO  - AUT [28037030]               |
| 111 | BELLEZA LA [28047080]                           |
| 112 | PUENTE CARRETERA [28047040]                     |
| 113 | CARACOLI - AUT [15067210]                       |
| 114 | CERCADO EL-AUTOMAT [15067020]                   |
| 115 | CORRAL DE PIEDRA [28017080]                     |
| 116 | EL SILENCIO - AUT [15067200]                    |
| 117 | MAGUEYES LOS [15067080]                         |
| 118 | POZO HONDO [15067130]                           |
| 119 | PUENTE GUAJIRO - AUT [15067150]                 |
| 120 | SAN FRANCISCO [15067170]                        |
| 121 | CORRAL DE PIEDRA  - AUT [28017140]              |
| 122 | AURORA LA [28047010]                            |
| 123 | CANAL FLORIDA [29067050]                        |
| 124 | EL BANCO - AUT [25027020]                       |
| 125 | FUNDACION [29067120]                            |
| 126 | PALMARIGUANI  - AUT [28047050]                  |
| 127 | PUERTO RICO HACIENDA  - AUT [29067060]          |
| 128 | RIO FRIO [29067070]                             |
| 129 | SANTA ROSALIA [29067040]                        |
| 130 | TREBOL EL [29067010]                            |
| 131 | GANADERIA CARIBE  - AUT [29067150]              |
| 132 | PUENTE FERROCARRIL [29067130]                   |
| 133 | PUENTE SEVILLA  - AUT [29067160]                |
| 134 | CABLE EL [16067020]                             |
| 135 | CAMPO SEIS [16037040]                           |
| 136 | PUENTE TARRA [16047020]                         |
| 137 | PUERTO BARCO-GABARRA - AUT [16067010]           |
| 138 | JAGUA LA [25020230]                             |
| 139 | LLANOS LOS [28020230]                           |
| 140 | LOMA LA [25020280]                              |
| 141 | MOLINO EL [28040310]                            |
| 142 | PASO EL   [28040350]                            |
| 143 | PLAYAS LAS HACIENDA [28020080]                  |
| 144 | SAN GABRIEL [28020420]                          |
| 145 | YUCAL EL [25021650]                             |
| 146 | BOSCONIA [28040030]                             |
| 147 | CODAZZI DC [28020460]                           |
| 148 | ESPERANZA LA HACIENDA [28020150]                |
| 149 | MANATURE HACIENDA [28040270]                    |
| 150 | PALMARIGUANI [28040070]                         |
| 151 | PALMASOLA [28040400]                            |
| 152 | RETORNO EL [28020600]                           |
| 153 | SANTA TERESA HACIENDA [28020440]                |
| 154 | BOGOTANA LA [28020310]                          |
| 155 | CARACOLI [28030190]                             |
| 156 | CHIMILAIMA [28040200]                           |
| 157 | LETICIA [28020590]                              |
| 158 | PARIS DE FRANCIA [28010370]                     |
| 159 | PAVAS LAS [28040060]                            |
| 160 | SAN BENITO [28020410]                           |
| 161 | VILLA MARLENE [28010070]                        |
| 162 | ATANQUEZ [28010360]                             |
| 163 | CUEVAS LAS [28040170]                           |
| 164 | DESCANSO EL [28010020]                          |
| 165 | MANAURE [28010040]                              |
| 166 | PUEBLO BELLO [28040010]                         |
| 167 | SAN ANGEL [28030220]                            |
| 168 | SAN SEBASTIAN DE [29060090]                     |
| 169 | VILLA CARMELITA [28010140]                      |
| 170 | PATILLAL [28010090]                             |
| 171 | PUEBLO BELLO  [28045010]                        |
| 172 | SARACHUI [28010130]                             |
| 173 | CANAVERALES [15060080]                          |
| 174 | CONEJO EL [15060150]                            |
| 175 | HATICO D LOS INDIO [28010200]                   |
| 176 | JUGUETE EL [15060070]                           |
| 177 | PAMPLONA [28010280]                             |
| 178 | SABANAS DE MANUELA [15060050]                   |
| 179 | VILLANUEVA [28010340]                           |
| 180 | BRILLANTE EL [28040320]                         |
| 181 | IRAN [25021620]                                 |
| 182 | MENCHIQUEJO [25021040]                          |
| 183 | NEGRITOS LOS [25021200]                         |
| 184 | PUEBLITO EL [25021500]                          |
| 185 | SAN ROQUE ALERTAS [25021380]                    |
| 186 | SAN SEBASTIAN [25020900]                        |
| 187 | VILLA CONCEPCION [28040300]                     |
| 188 | AGUADAS LAS ALERTA [25021540]                   |
| 189 | BARRANCO DE LOBA [25020880]                     |
| 190 | CHILLOA [25020890]                              |
| 191 | SUDAN EL [25021320]                             |
| 192 | GANAD LA ESMERALDA  [25020040]                  |
| 193 | PLAYITAS [25020870]                             |
| 194 | SANTA ROSA [25021090]                           |

</div>


<div align="center">

Records by parameter and station

</div>


<div align="center">

|                                                                                    |     0 |
|:-----------------------------------------------------------------------------------|------:|
| ('Caudal medio mensual', 'ALTO DEL ROSARIO [25027400]')                            |   574 |
| ('Caudal medio mensual', 'ARIGUANI HACIENDA - AUT [28017120]')                     |   230 |
| ('Caudal medio mensual', 'ARMENIA [25027360]')                                     |   546 |
| ('Caudal medio mensual', 'AURORA LA [28047010]')                                   |   664 |
| ('Caudal medio mensual', 'BECERRIL [28027050]')                                    |   529 |
| ('Caudal medio mensual', 'BELLEZA LA [28047080]')                                  |    96 |
| ('Caudal medio mensual', 'CABLE EL [16067020]')                                    |   424 |
| ('Caudal medio mensual', 'CAIMANCITO [25027590]')                                  |   411 |
| ('Caudal medio mensual', 'CAMPO SEIS [16037040]')                                  |   567 |
| ('Caudal medio mensual', 'CANAL FLORIDA [29067050]')                               |   574 |
| ('Caudal medio mensual', 'CANTACLARO [28037060]')                                  |   681 |
| ('Caudal medio mensual', 'CARACOLI - AUT [15067210]')                              |    28 |
| ('Caudal medio mensual', 'CERCADO EL-AUTOMAT [15067020]')                          |   568 |
| ('Caudal medio mensual', 'CHAPETONA LA [25027620]')                                |   487 |
| ('Caudal medio mensual', 'CHEMESQUEMENA [28017150]')                               |    53 |
| ('Caudal medio mensual', 'CONVENCION HACIENDA [28037020]')                         |   536 |
| ('Caudal medio mensual', 'CORRAL DE PIEDRA  - AUT [28017140]')                     |    41 |
| ('Caudal medio mensual', 'CORRAL DE PIEDRA [28017080]')                            |   705 |
| ('Caudal medio mensual', 'EL BANCO - AUT [25027020]')                              |   592 |
| ('Caudal medio mensual', 'EL SILENCIO - AUT [15067200]')                           |   115 |
| ('Caudal medio mensual', 'FLORES LAS [28027030]')                                  |   620 |
| ('Caudal medio mensual', 'FUNDACION [29067120]')                                   |   708 |
| ('Caudal medio mensual', 'GANADERIA CARIBE  - AUT [29067150]')                     |   662 |
| ('Caudal medio mensual', 'GRACIAS A DIOS HACIENDA [25027080]')                     |   497 |
| ('Caudal medio mensual', 'ISLANDIA [28027160]')                                    |   444 |
| ('Caudal medio mensual', 'LAS AGUADAS [25027490]')                                 |   589 |
| ('Caudal medio mensual', 'MAGUEYES LOS [15067080]')                                |   292 |
| ('Caudal medio mensual', 'MARIANGOLA [28037040]')                                  |   679 |
| ('Caudal medio mensual', 'MATILDE LA [28027020]')                                  |   579 |
| ('Caudal medio mensual', 'MINA LA [28017110]')                                     |   705 |
| ('Caudal medio mensual', 'PALMARIGUANI  - AUT [28047050]')                         |   632 |
| ('Caudal medio mensual', 'PALOMAS LAS [25027390]')                                 |   540 |
| ('Caudal medio mensual', 'PENONCITO [25027330]')                                   |   572 |
| ('Caudal medio mensual', 'POZO HONDO [15067130]')                                  |   388 |
| ('Caudal medio mensual', 'PUEBLO BELLO [28047020]')                                |   726 |
| ('Caudal medio mensual', 'PUENTE CALLAO [28037010]')                               |   647 |
| ('Caudal medio mensual', 'PUENTE CANOAS  - AUT [28037090]')                        |   590 |
| ('Caudal medio mensual', 'PUENTE CARRETERA [25027890]')                            |   448 |
| ('Caudal medio mensual', 'PUENTE CARRETERA [28037130]')                            |   603 |
| ('Caudal medio mensual', 'PUENTE CARRETERA [28047040]')                            |   499 |
| ('Caudal medio mensual', 'PUENTE FERROCARRIL [29067130]')                          |   657 |
| ('Caudal medio mensual', 'PUENTE GUAJIRO - AUT [15067150]')                        |   148 |
| ('Caudal medio mensual', 'PUENTE SALGUERO  - AUT [28037030]')                      |   727 |
| ('Caudal medio mensual', 'PUENTE SEVILLA  - AUT [29067160]')                       |   398 |
| ('Caudal medio mensual', 'PUENTE TARRA [16047020]')                                |   463 |
| ('Caudal medio mensual', 'PUERTO BARCO-GABARRA - AUT [16067010]')                  |   577 |
| ('Caudal medio mensual', 'PUERTO RICO HACIENDA  - AUT [29067060]')                 |   437 |
| ('Caudal medio mensual', 'REGIDOR [25027410]')                                     |   508 |
| ('Caudal medio mensual', 'REPOSO EL [28017050]')                                   |   443 |
| ('Caudal medio mensual', 'RIO FRIO [29067070]')                                    |   607 |
| ('Caudal medio mensual', 'RIO NUEVO [25027630]')                                   |   534 |
| ('Caudal medio mensual', 'SAN FRANCISCO [15067170]')                               |   157 |
| ('Caudal medio mensual', 'SAN ROQUE [25027320]')                                   |   560 |
| ('Caudal medio mensual', 'SANTA ROSALIA [29067040]')                               |   626 |
| ('Caudal medio mensual', 'SANTA TERESA [28027040]')                                |   628 |
| ('Caudal medio mensual', 'TREBOL EL [29067010]')                                   |   711 |
| ('Caudal medio mensual', 'VICTORIA LA [25027420]')                                 |   567 |
| ('Evaporación total diaria', 'LA GRAN VIA - AUT [29065130]')                       |  4822 |
| ('Precipitación total mensual', 'AEROPUERTO LAS FLORES [25025090]')                |   665 |
| ('Precipitación total mensual', 'AGUADAS LAS ALERTA [25021540]')                   |   504 |
| ('Precipitación total mensual', 'ASTREA [25020220]')                               |   718 |
| ('Precipitación total mensual', 'ATANQUEZ [28010360]')                             |   720 |
| ('Precipitación total mensual', 'BARRANCO DE LOBA [25020880]')                     |   553 |
| ('Precipitación total mensual', 'BAYANO [29060350]')                               |   522 |
| ('Precipitación total mensual', 'BELLAVISTA [28040150]')                           |   671 |
| ('Precipitación total mensual', 'BOGOTANA LA [28020310]')                          |   415 |
| ('Precipitación total mensual', 'BONGO EL [29060030]')                             |   555 |
| ('Precipitación total mensual', 'BOSCONIA [28040030]')                             |   500 |
| ('Precipitación total mensual', 'BRILLANTE EL [28040320]')                         |   575 |
| ('Precipitación total mensual', 'CABANA LA HACIENDA [28040360]')                   |   516 |
| ('Precipitación total mensual', 'CALLAO EL [28035020]')                            |   616 |
| ('Precipitación total mensual', 'CANAL EL [25020240]')                             |   705 |
| ('Precipitación total mensual', 'CANAVERALES [15060080]')                          |   700 |
| ('Precipitación total mensual', 'CARACOLI [28030190]')                             |   613 |
| ('Precipitación total mensual', 'CARMEN EL [29060140]')                            |   659 |
| ('Precipitación total mensual', 'CENIZO EL [29060060]')                            |   732 |
| ('Precipitación total mensual', 'CENTENARIO HACIENDA [28025090]')                  |   518 |
| ('Precipitación total mensual', 'CHILLOA [25020890]')                              |   534 |
| ('Precipitación total mensual', 'CHIMICHAGUA [25021240]')                          |   594 |
| ('Precipitación total mensual', 'CHIMILAIMA [28040200]')                           |   396 |
| ('Precipitación total mensual', 'CHIRIGUANA [25025250]')                           |   532 |
| ('Precipitación total mensual', 'CNO LA RAYA [16060010]')                          |   585 |
| ('Precipitación total mensual', 'CODAZZI DC [28020460]')                           |   498 |
| ('Precipitación total mensual', 'COLEGIO AGROPECUARIO PAILITAS  - AUT [25025330]') |   340 |
| ('Precipitación total mensual', 'CONEJO EL [15060150]')                            |   554 |
| ('Precipitación total mensual', 'CUEVAS LAS [28040170]')                           |   334 |
| ('Precipitación total mensual', 'CURUMANI D C [25021580]')                         |   188 |
| ('Precipitación total mensual', 'CURUMANI [25020250]')                             |   706 |
| ('Precipitación total mensual', 'DESCANSO EL [28010020]')                          |   359 |
| ('Precipitación total mensual', 'DESTINO EL [29060150]')                           |   644 |
| ('Precipitación total mensual', 'DONA MARIA [29060560]')                           |   443 |
| ('Precipitación total mensual', 'ENANO EL [29060160]')                             |   551 |
| ('Precipitación total mensual', 'ESPERANZA LA HACIENDA [28020150]')                |   500 |
| ('Precipitación total mensual', 'ESPERANZA LA [29060180]')                         |   558 |
| ('Precipitación total mensual', 'FLORIDA LA [29060190]')                           |   502 |
| ('Precipitación total mensual', 'FUNDACION [29060040]')                            |   776 |
| ('Precipitación total mensual', 'GANAD LA ESMERALDA  [25020040]')                  |   587 |
| ('Precipitación total mensual', 'GAVILAN [29060170]')                              |   660 |
| ('Precipitación total mensual', 'GLORIA LA [23210020]')                            |   298 |
| ('Precipitación total mensual', 'GUAYMARAL [28035040]')                            |   589 |
| ('Precipitación total mensual', 'HACHARIRA [16070030]')                            |   382 |
| ('Precipitación total mensual', 'HATICO D LOS INDIO [28010200]')                   |   588 |
| ('Precipitación total mensual', 'IRAN [25021620]')                                 |   469 |
| ('Precipitación total mensual', 'JAGUA LA [25020230]')                             |   685 |
| ('Precipitación total mensual', 'JUGUETE EL [15060070]')                           |   489 |
| ('Precipitación total mensual', 'LA GLORIA [23215060]')                            |   146 |
| ('Precipitación total mensual', 'LA PAULINA - AUT [15065040]')                     |   403 |
| ('Precipitación total mensual', 'LETICIA [28020590]')                              |   449 |
| ('Precipitación total mensual', 'LLANOS LOS [28020230]')                           |   481 |
| ('Precipitación total mensual', 'LOMA LA [25020280]')                              |   658 |
| ('Precipitación total mensual', 'MANATURE HACIENDA [28040270]')                    |   621 |
| ('Precipitación total mensual', 'MANAURE [28010040]')                              |   599 |
| ('Precipitación total mensual', 'MARIA LA [29060200]')                             |   545 |
| ('Precipitación total mensual', 'MATA LA [23215050]')                              |   529 |
| ('Precipitación total mensual', 'MENCHIQUEJO [25021040]')                          |   568 |
| ('Precipitación total mensual', 'MOLINO EL [28040310]')                            |   441 |
| ('Precipitación total mensual', 'MONTERRUBIO [28040100]')                          |   698 |
| ('Precipitación total mensual', 'MOTILONIA CODAZZI [28025070]')                    |   585 |
| ('Precipitación total mensual', 'NEGRITOS LOS [25021200]')                         |   525 |
| ('Precipitación total mensual', 'NUEVA GRANADA [25021630]')                        |   461 |
| ('Precipitación total mensual', 'ORU [16070040]')                                  |   551 |
| ('Precipitación total mensual', 'PADELMA [29065020]')                              |   641 |
| ('Precipitación total mensual', 'PALACIO EL [16050240]')                           |   335 |
| ('Precipitación total mensual', 'PALMA LA [29060210]')                             |   656 |
| ('Precipitación total mensual', 'PALMARIGUANI [28040070]')                         |   699 |
| ('Precipitación total mensual', 'PALMASOLA [28040400]')                            |   358 |
| ('Precipitación total mensual', 'PALMOR EL [29060340]')                            |   530 |
| ('Precipitación total mensual', 'PALO ALTO [29060270]')                            |   658 |
| ('Precipitación total mensual', 'PAMPLONA [28010280]')                             |   118 |
| ('Precipitación total mensual', 'PARIS DE FRANCIA [28010370]')                     |   538 |
| ('Precipitación total mensual', 'PASO EL   [28040350]')                            |   591 |
| ('Precipitación total mensual', 'PATILLAL [28010090]')                             |   679 |
| ('Precipitación total mensual', 'PAVAS LAS [28040060]')                            |   344 |
| ('Precipitación total mensual', 'PISTA LA [16070020]')                             |   154 |
| ('Precipitación total mensual', 'PLAYA LA [29060330]')                             |   252 |
| ('Precipitación total mensual', 'PLAYAS LAS HACIENDA [28020080]')                  |   598 |
| ('Precipitación total mensual', 'PLAYITAS [25020870]')                             |   561 |
| ('Precipitación total mensual', 'POLY LA [29060220]')                              |   354 |
| ('Precipitación total mensual', 'POPONTE [25020690]')                              |   583 |
| ('Precipitación total mensual', 'PRADO SEVILLA [29065030]')                        |   530 |
| ('Precipitación total mensual', 'PRIMAVERA LA [25020920]')                         |   506 |
| ('Precipitación total mensual', 'PROYECTOS LOS [29060250]')                        |   656 |
| ('Precipitación total mensual', 'PUEBLITO EL [25021500]')                          |   531 |
| ('Precipitación total mensual', 'PUEBLO BELLO  [28045010]')                        |   526 |
| ('Precipitación total mensual', 'PUEBLO BELLO [28040010]')                         |   709 |
| ('Precipitación total mensual', 'PUERTO BARCO [16070010]')                         |   518 |
| ('Precipitación total mensual', 'RAYA LA [25020670]')                              |   549 |
| ('Precipitación total mensual', 'RETORNO EL [28020600]')                           |   589 |
| ('Precipitación total mensual', 'RINCON EL [28025020]')                            |   686 |
| ('Precipitación total mensual', 'RINCONHONDO [25020260]')                          |   700 |
| ('Precipitación total mensual', 'RUBY EL [29060550]')                              |   360 |
| ('Precipitación total mensual', 'SABANAS DE MANUELA [15060050]')                   |   678 |
| ('Precipitación total mensual', 'SALOA [25020270]')                                |   714 |
| ('Precipitación total mensual', 'SAN ANGEL [28030220]')                            |   401 |
| ('Precipitación total mensual', 'SAN ANGEL [28040140]')                            |   665 |
| ('Precipitación total mensual', 'SAN BENITO [28020410]')                           |   539 |
| ('Precipitación total mensual', 'SAN GABRIEL [28020420]')                          |   529 |
| ('Precipitación total mensual', 'SAN ISIDRO [29060280]')                           |   640 |
| ('Precipitación total mensual', 'SAN JOSE D ORIENTE [28025040]')                   |   237 |
| ('Precipitación total mensual', 'SAN JUAN [29060290]')                             |   305 |
| ('Precipitación total mensual', 'SAN PABLO [29060070]')                            |   723 |
| ('Precipitación total mensual', 'SAN ROQUE ALERTAS [25021380]')                    |   478 |
| ('Precipitación total mensual', 'SAN SEBASTIAN DE [29060090]')                     |   574 |
| ('Precipitación total mensual', 'SAN SEBASTIAN [25020900]')                        |   547 |
| ('Precipitación total mensual', 'SANTA ISABEL [25021640]')                         |   444 |
| ('Precipitación total mensual', 'SANTA ROSA DE LIMA [29060100]')                   |   568 |
| ('Precipitación total mensual', 'SANTA ROSA [25021090]')                           |   537 |
| ('Precipitación total mensual', 'SANTA TERESA HACIENDA [28020440]')                |   730 |
| ('Precipitación total mensual', 'SARA LA [29060230]')                              |   471 |
| ('Precipitación total mensual', 'SARACHUI [28010130]')                             |   263 |
| ('Precipitación total mensual', 'SEIS EL [25025300]')                              |   510 |
| ('Precipitación total mensual', 'SEVILLANO [29060310]')                            |   538 |
| ('Precipitación total mensual', 'SOCOMBA [28025080]')                              |   389 |
| ('Precipitación total mensual', 'SUDAN EL [25021320]')                             |   530 |
| ('Precipitación total mensual', 'TAMALAMEQUE D C [25021590]')                      |   361 |
| ('Precipitación total mensual', 'TAMALAMEQUE [25020090]')                          |   741 |
| ('Precipitación total mensual', 'TASAJERA [29060120]')                             |   678 |
| ('Precipitación total mensual', 'TERROR EL HACIENDA [25020650]')                   |   524 |
| ('Precipitación total mensual', 'UNION LA [29060240]')                             |   597 |
| ('Precipitación total mensual', 'URUMITA [28015070]')                              |   550 |
| ('Precipitación total mensual', 'VILLA CARMELITA [28010140]')                      |   388 |
| ('Precipitación total mensual', 'VILLA CONCEPCION [28040300]')                     |   564 |
| ('Precipitación total mensual', 'VILLA MARLENE [28010070]')                        |   619 |
| ('Precipitación total mensual', 'VILLA ROSA [28035010]')                           |   604 |
| ('Precipitación total mensual', 'VILLANUEVA [28010340]')                           |   578 |
| ('Precipitación total mensual', 'YE LA [15015020]')                                |   484 |
| ('Precipitación total mensual', 'YUCAL EL [25021650]')                             |   443 |
| ('Precipitación total mensual', 'ZACAPA [29065010]')                               |   308 |
| ('Precipitación total mensual', 'ZAPATOZA [25020660]')                             |   587 |
| ('Temperatura máxima diaria', 'AEROPUERTO ALFONSO LOPEZ - [28025502]')             | 12709 |
| ('Temperatura máxima diaria', 'AEROPUERTO LAS FLORES [25025090]')                  |  8874 |
| ('Temperatura máxima diaria', 'ALGARROBO [28045020]')                              |  1050 |
| ('Temperatura máxima diaria', 'CALLAO EL [28035020]')                              | 12394 |
| ('Temperatura máxima diaria', 'CENTENARIO HACIENDA [28025090]')                    | 13070 |
| ('Temperatura máxima diaria', 'CHIRIGUANA [25025250]')                             | 11914 |
| ('Temperatura máxima diaria', 'CICOLAC [28015030]')                                |  1148 |
| ('Temperatura máxima diaria', 'COLEGIO AGROPECUARIO PAILITAS  - AUT [25025330]')   |  7606 |
| ('Temperatura máxima diaria', 'GUAIRA LA HACIENDA [28045040]')                     |   784 |
| ('Temperatura máxima diaria', 'GUATAPURI - AUT [28035070]')                        |    42 |
| ('Temperatura máxima diaria', 'GUAYMARAL [28035040]')                              |  9470 |
| ('Temperatura máxima diaria', 'LA GLORIA [23215060]')                              |   960 |
| ('Temperatura máxima diaria', 'LA PAULINA - AUT [15065040]')                       |  4285 |
| ('Temperatura máxima diaria', 'LOS ALAMOS - AUT [25025002]')                       |  7702 |
| ('Temperatura máxima diaria', 'MOTILONIA CODAZZI [28025070]')                      | 13951 |
| ('Temperatura máxima diaria', 'PADELMA [29065020]')                                |  9853 |
| ('Temperatura máxima diaria', 'PRADO SEVILLA [29065030]')                          | 11118 |
| ('Temperatura máxima diaria', 'RINCON EL [28025020]')                              | 13407 |
| ('Temperatura máxima diaria', 'SAN JOSE D ORIENTE [28025040]')                     |  3056 |
| ('Temperatura máxima diaria', 'SEIS EL [25025300]')                                | 10067 |
| ('Temperatura máxima diaria', 'SOCOMBA [28025080]')                                |  7504 |
| ('Temperatura máxima diaria', 'URUMITA [28015070]')                                | 13322 |
| ('Temperatura máxima diaria', 'VILLA ROSA [28035010]')                             |  8442 |
| ('Temperatura máxima diaria', 'YE LA [15015020]')                                  | 10090 |
| ('Temperatura máxima diaria', 'ZACAPA [29065010]')                                 |  1239 |
| ('Temperatura mínima diaria', 'AEROPUERTO ALFONSO LOPEZ - [28025502]')             | 13496 |
| ('Temperatura mínima diaria', 'AEROPUERTO LAS FLORES [25025090]')                  | 10055 |
| ('Temperatura mínima diaria', 'ALGARROBO [28045020]')                              |  1052 |
| ('Temperatura mínima diaria', 'CALLAO EL [28035020]')                              | 11958 |
| ('Temperatura mínima diaria', 'CENTENARIO HACIENDA [28025090]')                    | 11991 |
| ('Temperatura mínima diaria', 'CHIRIGUANA [25025250]')                             | 12540 |
| ('Temperatura mínima diaria', 'CICOLAC [28015030]')                                |  1428 |
| ('Temperatura mínima diaria', 'COLEGIO AGROPECUARIO PAILITAS  - AUT [25025330]')   |  9275 |
| ('Temperatura mínima diaria', 'GUAIRA LA HACIENDA [28045040]')                     |  1274 |
| ('Temperatura mínima diaria', 'GUATAPURI - AUT [28035070]')                        |    42 |
| ('Temperatura mínima diaria', 'GUAYMARAL [28035040]')                              | 13461 |
| ('Temperatura mínima diaria', 'LA GLORIA [23215060]')                              |  1248 |
| ('Temperatura mínima diaria', 'LA PAULINA - AUT [15065040]')                       |  5799 |
| ('Temperatura mínima diaria', 'LOS ALAMOS - AUT [25025002]')                       | 10734 |
| ('Temperatura mínima diaria', 'MOTILONIA CODAZZI [28025070]')                      | 14405 |
| ('Temperatura mínima diaria', 'PADELMA [29065020]')                                | 13432 |
| ('Temperatura mínima diaria', 'PRADO SEVILLA [29065030]')                          | 12117 |
| ('Temperatura mínima diaria', 'RINCON EL [28025020]')                              | 13900 |
| ('Temperatura mínima diaria', 'SAN JOSE D ORIENTE [28025040]')                     |  3644 |
| ('Temperatura mínima diaria', 'SEIS EL [25025300]')                                | 11694 |
| ('Temperatura mínima diaria', 'SOCOMBA [28025080]')                                |  8056 |
| ('Temperatura mínima diaria', 'URUMITA [28015070]')                                | 13107 |
| ('Temperatura mínima diaria', 'VILLA ROSA [28035010]')                             | 10558 |
| ('Temperatura mínima diaria', 'YE LA [15015020]')                                  | 11197 |
| ('Temperatura mínima diaria', 'ZACAPA [29065010]')                                 |  1393 |

</div>



### Analysis from 1980 to 2021 for Etiqueta == "PTPM_TT_M": 55363 (10.75%)

Pivot table: [Pivot_PTPM_TT_M.csv](Pivot_PTPM_TT_M.csv)
![R.LTWB](Graph/Plot_PTPM_TT_M_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: COLEGIO AGROPECUARIO PAILITAS  - AUT [25025330] (339 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=8.954222222,-73.63008333) or [Openstreet Map](https://www.openstreetmap.org/query?lat=8.954222222&lon=-73.63008333)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion                                  |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------------------------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1987-12-01 00:00:00 |         25025330 | COLEGIO AGROPECUARIO PAILITAS  - AUT [25025330] |   8.95422 |   -73.6301 |        50 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Pailitas    | 1987-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |     202 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 339     |
| mean  | 164.522 |
| std   | 130.426 |
| min   |   0     |
| 25%   |  59.8   |
| 50%   | 142     |
| 75%   | 252.9   |
| max   | 693     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_25025330_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25025330_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25025330_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25025330_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: GLORIA LA [23210020] (297 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=8.630555556,-73.80416667) or [Openstreet Map](https://www.openstreetmap.org/query?lat=8.630555556&lon=-73.80416667)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                          | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:---------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1995-05-01 00:00:00 |         23210020 | GLORIA LA [23210020] |   8.63056 |   -73.8042 |        40 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 08 - Santanderes-Arauca | Cesar          | La Gloria   | 1995-05-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |     183 |       4 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 297     |
| mean  | 159.691 |
| std   | 137.871 |
| min   |   0     |
| 25%   |  45     |
| 50%   | 130     |
| 75%   | 241     |
| max   | 649     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_23210020_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_23210020_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_23210020_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_23210020_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: LA GLORIA [23215060] (146 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=8.615277778,-73.800555556) or [Openstreet Map](https://www.openstreetmap.org/query?lat=8.615277778&lon=-73.800555556)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                          | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:---------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1983-10-01 00:00:00 |         23215060 | LA GLORIA [23215060] |   8.61528 |   -73.8006 |        35 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 08 - Santanderes-Arauca | Cesar          | La Gloria   | 1995-05-15 00:00:00 | 2018-06-19 10:35:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |   126.2 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 146     |
| mean  | 136.245 |
| std   | 106.68  |
| min   |   0     |
| 25%   |  46.55  |
| 50%   | 122.9   |
| 75%   | 196.125 |
| max   | 422     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_23215060_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_23215060_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_23215060_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_23215060_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: MATA LA [23215050] (467 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=8.614444444,-73.63638889) or [Openstreet Map](https://www.openstreetmap.org/query?lat=8.614444444&lon=-73.63638889)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion     |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                          | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:---------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         23215050 | MATA LA [23215050] |   8.61444 |   -73.6364 |       163 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 08 - Santanderes-Arauca | Cesar          | La Gloria   | 1983-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      50 |       4 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count |  467     |
| mean  |  233.842 |
| std   |  212.824 |
| min   |    0     |
| 25%   |   74.5   |
| 50%   |  182.3   |
| 75%   |  332.85  |
| max   | 1094.2   |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_23215050_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_23215050_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_23215050_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_23215050_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: RAYA LA [25020670] (466 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.050277778,-73.55972222) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.050277778&lon=-73.55972222)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion     |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25020670 | RAYA LA [25020670] |   9.05028 |   -73.5597 |       500 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Pailitas    | 1972-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 466     |
| mean  | 146.059 |
| std   | 129.158 |
| min   |   0     |
| 25%   |  33     |
| 50%   | 118     |
| 75%   | 238.5   |
| max   | 814     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_25020670_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020670_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020670_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020670_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: SANTA ISABEL [25021640] (443 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=8.71275,-73.70255556) or [Openstreet Map](https://www.openstreetmap.org/query?lat=8.71275&lon=-73.70255556)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion          |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1984-12-01 00:00:00 |         25021640 | SANTA ISABEL [25021640] |   8.71275 |   -73.7026 |        40 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Pelaya      | 1984-11-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 443     |
| mean  | 145.321 |
| std   | 132.377 |
| min   |   0     |
| 25%   |  38.35  |
| 50%   | 115.5   |
| 75%   | 213.5   |
| max   | 717     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_25021640_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021640_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021640_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021640_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: TAMALAMEQUE D C [25021590] (206 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=8.866666667,-73.81666667) or [Openstreet Map](https://www.openstreetmap.org/query?lat=8.866666667&lon=-73.81666667)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion             |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25021590 | TAMALAMEQUE D C [25021590] |   8.86667 |   -73.8167 |        33 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Tamalameque | 1979-11-15 00:00:00 | 1998-06-15 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 206     |
| mean  | 136.508 |
| std   | 112.785 |
| min   |   0     |
| 25%   |  36.5   |
| 50%   | 125.8   |
| 75%   | 208.725 |
| max   | 512.2   |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_25021590_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021590_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021590_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021590_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: TAMALAMEQUE [25020090] (501 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=8.860388889,-73.81544444) or [Openstreet Map](https://www.openstreetmap.org/query?lat=8.860388889&lon=-73.81544444)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion         |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-----------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25020090 | TAMALAMEQUE [25020090] |   8.86039 |   -73.8154 |        20 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Tamalameque | 1960-02-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 501     |
| mean  | 163.094 |
| std   | 143.448 |
| min   |   0     |
| 25%   |  44.7   |
| 50%   | 139     |
| 75%   | 246.6   |
| max   | 870.6   |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_25020090_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020090_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020090_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020090_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: TERROR EL HACIENDA [25020650] (436 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=8.938777778,-73.56022222) or [Openstreet Map](https://www.openstreetmap.org/query?lat=8.938777778&lon=-73.56022222)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion                |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25020650 | TERROR EL HACIENDA [25020650] |   8.93878 |   -73.5602 |       250 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Chimichagua | 1972-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      11 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count |  436     |
| mean  |  156.154 |
| std   |  178.632 |
| min   |    0     |
| 25%   |   30.675 |
| 50%   |  115     |
| 75%   |  226.925 |
| max   | 1585     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_25020650_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020650_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020650_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020650_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: ZAPATOZA [25020660] (502 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.00975,-73.75402778) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.00975&lon=-73.75402778)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion      |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:--------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25020660 | ZAPATOZA [25020660] |   9.00975 |    -73.754 |        90 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Curumaní    | 1972-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       1 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 502     |
| mean  | 155.621 |
| std   | 132.496 |
| min   |   0     |
| 25%   |  49.175 |
| 50%   | 127.1   |
| 75%   | 230     |
| max   | 679     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_25020660_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020660_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020660_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020660_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: BELLAVISTA [28040150] (466 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.30805556,-74.03922222) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.30805556&lon=-74.03922222)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion        |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28040150 | BELLAVISTA [28040150] |   10.3081 |   -74.0392 |       140 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Algarrobo   | 1963-02-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       9 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 466     |
| mean  | 116.057 |
| std   |  94.465 |
| min   |   0     |
| 25%   |  42.25  |
| 50%   | 107     |
| 75%   | 163.75  |
| max   | 710     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_28040150_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040150_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040150_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040150_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: CABANA LA HACIENDA [28040360] (503 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.861,-74.07672222) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.861&lon=-74.07672222)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion                |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio             | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:----------------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28040360 | CABANA LA HACIENDA [28040360] |     9.861 |   -74.0767 |       100 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Ariguaní (El Dificil) | 1979-01-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      10 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 503      |
| mean  | 124.758  |
| std   |  95.0967 |
| min   |   0      |
| 25%   |  52.5    |
| 50%   | 116      |
| 75%   | 174      |
| max   | 840      |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_28040360_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040360_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040360_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040360_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: DESTINO EL [29060150] (488 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.57366667,-74.22411111) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.57366667&lon=-74.22411111)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion        |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29060150 | DESTINO EL [29060150] |   10.5737 |   -74.2241 |        20 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | El Retén    | 1967-01-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 488     |
| mean  | 134.827 |
| std   | 133.877 |
| min   |   0     |
| 25%   |  21.75  |
| 50%   | 100.5   |
| 75%   | 217.25  |
| max   | 861     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_29060150_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060150_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060150_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060150_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: DONA MARIA [29060560] (442 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.38444444,-74.17794444) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.38444444&lon=-74.17794444)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion        |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1984-12-01 00:00:00 |         29060560 | DONA MARIA [29060560] |   10.3844 |   -74.1779 |        50 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Fundación   | 1984-11-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 442      |
| mean  |  97.6916 |
| std   | 101.206  |
| min   |   0      |
| 25%   |  16      |
| 50%   |  68.5    |
| 75%   | 150      |
| max   | 718      |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_29060560_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060560_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060560_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060560_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: FUNDACION [29060040] (499 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.52436111,-74.18222222) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.52436111&lon=-74.18222222)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29060040 | FUNDACION [29060040] |   10.5244 |   -74.1822 |        40 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Fundación   | 1958-03-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      15 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 499     |
| mean  | 119.442 |
| std   | 115.678 |
| min   |   0     |
| 25%   |  28     |
| 50%   |  97     |
| 75%   | 172.5   |
| max   | 757.5   |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_29060040_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060040_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060040_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060040_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: MARIA LA [29060200] (483 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.54066667,-74.18697222) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.54066667&lon=-74.18697222)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion      |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:--------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29060200 | MARIA LA [29060200] |   10.5407 |    -74.187 |        30 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Aracataca   | 1974-11-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 483     |
| mean  | 118.879 |
| std   | 114.639 |
| min   |   0     |
| 25%   |  24     |
| 50%   | 100     |
| 75%   | 178.5   |
| max   | 685     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_29060200_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060200_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060200_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060200_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: MONTERRUBIO [28040100] (493 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.23369444,-74.27325) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.23369444&lon=-74.27325)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion         |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-----------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28040100 | MONTERRUBIO [28040100] |   10.2337 |   -74.2733 |       100 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Pivijai     | 1963-01-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      83 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 493     |
| mean  | 144.448 |
| std   | 109.05  |
| min   |   0     |
| 25%   |  54     |
| 50%   | 137     |
| 75%   | 209     |
| max   | 741     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_28040100_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040100_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040100_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040100_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: NUEVA GRANADA [25021630] (460 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.80175,-74.38855556) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.80175&lon=-74.38855556)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion           |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio     | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:--------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1982-07-01 00:00:00 |         25021630 | NUEVA GRANADA [25021630] |   9.80175 |   -74.3886 |       110 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Nueva Granada | 1982-06-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |     123 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 460      |
| mean  | 111.086  |
| std   |  78.2969 |
| min   |   0      |
| 25%   |  49      |
| 50%   |  99      |
| 75%   | 165.25   |
| max   | 370      |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_25021630_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021630_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021630_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021630_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: SAN ANGEL [28040140] (484 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.03305556,-74.21261111) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.03305556&lon=-74.21261111)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio            | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:---------------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28040140 | SAN ANGEL [28040140] |   10.0331 |   -74.2126 |       140 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Sabanas De San Ángel | 1963-01-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       6 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 484      |
| mean  |  96.3804 |
| std   |  86.5089 |
| min   |   0      |
| 25%   |  23.9    |
| 50%   |  76.15   |
| 75%   | 145      |
| max   | 435      |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_28040140_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040140_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040140_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040140_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: SANTA ROSA DE LIMA [29060100] (504 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.40275,-74.108) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.40275&lon=-74.108)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion                |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29060100 | SANTA ROSA DE LIMA [29060100] |   10.4027 |    -74.108 |        75 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Fundación   | 1975-08-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      75 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 504     |
| mean  | 130.562 |
| std   | 109.441 |
| min   |   0     |
| 25%   |  40     |
| 50%   | 117.5   |
| 75%   | 189     |
| max   | 665     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_29060100_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060100_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060100_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060100_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: BAYANO [29060350] (461 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.63116667,-74.29858333) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.63116667&lon=-74.29858333)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion    |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29060350 | BAYANO [29060350] |   10.6312 |   -74.2986 |        30 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | El Retén    | 1975-01-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 461     |
| mean  | 107.534 |
| std   | 115.366 |
| min   |   0     |
| 25%   |   5.4   |
| 50%   |  76.7   |
| 75%   | 171     |
| max   | 711     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_29060350_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060350_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060350_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060350_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: BONGO EL [29060030] (503 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.64877778,-74.3755) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.64877778&lon=-74.3755)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion      |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:--------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29060030 | BONGO EL [29060030] |   10.6488 |   -74.3755 |        20 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | El Retén    | 1975-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 503     |
| mean  | 112.185 |
| std   | 120.076 |
| min   |   0     |
| 25%   |   5.5   |
| 50%   |  84.2   |
| 75%   | 174.5   |
| max   | 750     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_29060030_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060030_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060030_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060030_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: CARMEN EL [29060140] (503 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.6755,-74.20644444) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.6755&lon=-74.20644444)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio     | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:--------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29060140 | CARMEN EL [29060140] |   10.6755 |   -74.2064 |        25 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1967-03-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      14 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count |  503     |
| mean  |  131.782 |
| std   |  154.306 |
| min   |    0     |
| 25%   |    7.5   |
| 50%   |   87     |
| 75%   |  201     |
| max   | 1116     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_29060140_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060140_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060140_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060140_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: CENIZO EL [29060060] (492 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.65161111,-74.07322222) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.65161111&lon=-74.07322222)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29060060 | CENIZO EL [29060060] |   10.6516 |   -74.0732 |       450 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Aracataca   | 1959-03-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       8 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 492     |
| mean  | 214.417 |
| std   | 188.986 |
| min   |   0     |
| 25%   |  50     |
| 50%   | 180     |
| 75%   | 325     |
| max   | 944     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_29060060_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060060_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060060_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060060_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: FLORIDA LA [29060190] (420 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.61063889,-74.25538889) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.61063889&lon=-74.25538889)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion        |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29060190 | FLORIDA LA [29060190] |   10.6106 |   -74.2554 |        26 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | El Retén    | 1973-04-15 00:00:00 | 2019-02-07 11:43:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       6 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 420     |
| mean  | 106.892 |
| std   | 119.315 |
| min   |   0     |
| 25%   |   4.75  |
| 50%   |  71.5   |
| 75%   | 158.25  |
| max   | 794     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_29060190_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060190_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060190_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060190_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: GAVILAN [29060170] (503 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.68044444,-74.33069444) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.68044444&lon=-74.33069444)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion     |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29060170 | GAVILAN [29060170] |   10.6804 |   -74.3307 |        20 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | El Retén    | 1967-03-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 503      |
| mean  |  79.0485 |
| std   |  92.832  |
| min   |   0      |
| 25%   |   0      |
| 50%   |  46      |
| 75%   | 134.15   |
| max   | 534.1    |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_29060170_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060170_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060170_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060170_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: PADELMA [29065020] (490 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.72111111,-74.19972222) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.72111111&lon=-74.19972222)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion     |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio     | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:--------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29065020 | PADELMA [29065020] |   10.7211 |   -74.1997 |        20 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1967-08-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |     3.3 |       4 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 490     |
| mean  | 102.09  |
| std   | 105.756 |
| min   |   0     |
| 25%   |   9.475 |
| 50%   |  74.05  |
| 75%   | 158.575 |
| max   | 563.1   |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_29065020_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29065020_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29065020_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29065020_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: PALO ALTO [29060270] (501 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.7225,-74.27191667) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.7225&lon=-74.27191667)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29060270 | PALO ALTO [29060270] |   10.7225 |   -74.2719 |        25 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Puebloviejo | 1967-01-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 501      |
| mean  |  86.9663 |
| std   |  99.7629 |
| min   |   0      |
| 25%   |   0      |
| 50%   |  56      |
| 75%   | 132      |
| max   | 519      |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_29060270_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060270_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060270_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060270_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: UNION LA [29060240] (441 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.70655556,-74.22355556) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.70655556&lon=-74.22355556)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion      |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio     | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:--------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:--------------|:--------------------|:--------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29060240 | UNION LA [29060240] |   10.7066 |   -74.2236 |        20 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1967-01-15 00:00:00 | 2019-02-07 11:43:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count |  441     |
| mean  |  105.639 |
| std   |  136.714 |
| min   |    0     |
| 25%   |    0     |
| 50%   |   67     |
| 75%   |  170     |
| max   | 1016     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_29060240_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060240_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060240_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060240_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: ZACAPA [29065010] (122 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.58333333,-74.25) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.58333333&lon=-74.25)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion    |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29065010 | ZACAPA [29065010] |   10.5833 |     -74.25 |        30 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | El Retén    | 1967-07-15 00:00:00 | 1990-04-15 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |       4 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 122      |
| mean  |  93.5492 |
| std   |  92.2916 |
| min   |   0      |
| 25%   |  11.1    |
| 50%   |  70.65   |
| 75%   | 151.225  |
| max   | 366.7    |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_29065010_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29065010_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29065010_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29065010_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: ESPERANZA LA [29060180] (500 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.74252778,-74.30627778) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.74252778&lon=-74.30627778)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion          |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29060180 | ESPERANZA LA [29060180] |   10.7425 |   -74.3063 |        25 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Puebloviejo | 1975-10-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count |  500     |
| mean  |  116.55  |
| std   |  151.057 |
| min   |    0     |
| 25%   |    0     |
| 50%   |   69.5   |
| 75%   |  168     |
| max   | 1075     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_29060180_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060180_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060180_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060180_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: PALMOR EL [29060340] (490 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.77344444,-74.02563889) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.77344444&lon=-74.02563889)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29060340 | PALMOR EL [29060340] |   10.7734 |   -74.0256 |      1200 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Ciénaga     | 1975-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      67 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 490     |
| mean  | 192.753 |
| std   | 165.79  |
| min   |   0     |
| 25%   |  52.5   |
| 50%   | 165.5   |
| 75%   | 282.75  |
| max   | 875     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_29060340_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060340_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060340_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060340_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: PLAYA LA [29060330] (252 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.76197222,-74.12047222) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.76197222&lon=-74.12047222)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion      |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio     | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:--------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:--------------|:--------------------|:--------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1990-01-01 00:00:00 |         29060330 | PLAYA LA [29060330] |    10.762 |   -74.1205 |        20 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1990-01-15 00:00:00 | 2019-02-07 11:32:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |       4 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 252     |
| mean  | 131.828 |
| std   | 139.738 |
| min   |   0     |
| 25%   |  11.5   |
| 50%   |  97     |
| 75%   | 208.25  |
| max   | 615     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_29060330_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060330_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060330_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060330_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: POLY LA [29060220] (258 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.81666667,-74.18333333) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.81666667&lon=-74.18333333)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion     |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio     | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:--------------|:--------------------|:--------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29060220 | POLY LA [29060220] |   10.8167 |   -74.1833 |        24 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1972-01-15 00:00:00 | 2002-02-15 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 258     |
| mean  | 114.547 |
| std   | 152.219 |
| min   |   0     |
| 25%   |   0     |
| 50%   |  64.5   |
| 75%   | 157.75  |
| max   | 941     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_29060220_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060220_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060220_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060220_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: PRADO SEVILLA [29065030] (412 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.76416667,-74.15472222) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.76416667&lon=-74.15472222)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion           |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio     | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:--------------|:--------------------|:--------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29065030 | PRADO SEVILLA [29065030] |   10.7642 |   -74.1547 |        18 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1970-07-15 00:00:00 | 2019-02-07 11:32:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 412     |
| mean  | 121.007 |
| std   | 122.086 |
| min   |   0     |
| 25%   |  11.3   |
| 50%   |  96.5   |
| 75%   | 179.975 |
| max   | 637.9   |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_29065030_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29065030_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29065030_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29065030_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: PROYECTOS LOS [29060250] (499 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.73672222,-74.23708333) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.73672222&lon=-74.23708333)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion           |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio     | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:--------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29060250 | PROYECTOS LOS [29060250] |   10.7367 |   -74.2371 |        20 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1967-01-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 499      |
| mean  |  82.9495 |
| std   | 102.98   |
| min   |   0      |
| 25%   |   0      |
| 50%   |  50      |
| 75%   | 122.05   |
| max   | 627.6    |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_29060250_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060250_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060250_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060250_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: RUBY EL [29060550] (360 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.84513889,-74.18822222) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.84513889&lon=-74.18822222)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion     |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio     | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:--------------|:--------------------|:--------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1984-04-01 00:00:00 |         29060550 | RUBY EL [29060550] |   10.8451 |   -74.1882 |        20 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1984-03-15 00:00:00 | 2019-02-07 11:33:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       4 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 360      |
| mean  |  97.5958 |
| std   | 110.703  |
| min   |   0      |
| 25%   |   0      |
| 50%   |  68      |
| 75%   | 160.05   |
| max   | 652      |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_29060550_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060550_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060550_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060550_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: SAN JUAN [29060290] (249 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.76666667,-74.16666667) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.76666667&lon=-74.16666667)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion      |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio     | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:--------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:--------------|:--------------------|:--------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29060290 | SAN JUAN [29060290] |   10.7667 |   -74.1667 |        25 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1975-05-15 00:00:00 | 2002-02-15 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 249     |
| mean  | 103.559 |
| std   | 124.612 |
| min   |   0     |
| 25%   |   0     |
| 50%   |  60     |
| 75%   | 149     |
| max   | 627     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_29060290_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060290_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060290_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060290_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: SAN PABLO [29060070] (502 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.80819444,-74.02680556) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.80819444&lon=-74.02680556)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29060070 | SAN PABLO [29060070] |   10.8082 |   -74.0268 |       800 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Ciénaga     | 1960-08-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |    24.3 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 502     |
| mean  | 199.184 |
| std   | 159.074 |
| min   |   0     |
| 25%   |  61.5   |
| 50%   | 179     |
| 75%   | 306     |
| max   | 927     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_29060070_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060070_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060070_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060070_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: SARA LA [29060230] (370 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.83622222,-74.16102778) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.83622222&lon=-74.16102778)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion     |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio     | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:--------------|:--------------------|:--------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29060230 | SARA LA [29060230] |   10.8362 |    -74.161 |        25 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1971-08-15 00:00:00 | 2019-02-07 11:33:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 370     |
| mean  | 101.154 |
| std   | 108.271 |
| min   |   0     |
| 25%   |   6     |
| 50%   |  72     |
| 75%   | 158.5   |
| max   | 549     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_29060230_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060230_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060230_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060230_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: ENANO EL [29060160] (489 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.90219444,-74.18947222) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.90219444&lon=-74.18947222)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion      |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio     | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:--------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:--------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29060160 | ENANO EL [29060160] |   10.9022 |   -74.1895 |        25 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1974-11-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 489     |
| mean  |  83.846 |
| std   | 104.429 |
| min   |   0     |
| 25%   |   0     |
| 50%   |  40     |
| 75%   | 136.1   |
| max   | 655.1   |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_29060160_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060160_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060160_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060160_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: PALMA LA [29060210] (501 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.96683333,-74.20469444) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.96683333&lon=-74.20469444)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion      |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:--------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29060210 | PALMA LA [29060210] |   10.9668 |   -74.2047 |        23 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Ciénaga     | 1967-03-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 501      |
| mean  |  70.4112 |
| std   |  85.1528 |
| min   |   0      |
| 25%   |   1.2    |
| 50%   |  39.4    |
| 75%   | 108.6    |
| max   | 549.8    |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_29060210_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060210_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060210_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060210_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: SAN ISIDRO [29060280] (484 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.90083333,-74.22061111) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.90083333&lon=-74.22061111)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion        |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio     | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:--------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29060280 | SAN ISIDRO [29060280] |   10.9008 |   -74.2206 |        25 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1967-01-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 484      |
| mean  |  69.8316 |
| std   |  89.7702 |
| min   |   0      |
| 25%   |   0      |
| 50%   |  35.2    |
| 75%   | 110.625  |
| max   | 630.2    |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_29060280_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060280_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060280_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060280_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: SEVILLANO [29060310] (504 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.93305556,-74.25244444) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.93305556&lon=-74.25244444)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29060310 | SEVILLANO [29060310] |   10.9331 |   -74.2524 |         5 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Ciénaga     | 1979-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 504      |
| mean  |  79.7937 |
| std   | 116.537  |
| min   |   0      |
| 25%   |   0      |
| 50%   |  33      |
| 75%   | 128      |
| max   | 930      |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_29060310_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060310_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060310_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060310_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: TASAJERA [29060120] (504 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.97622222,-74.36175) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.97622222&lon=-74.36175)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion      |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:--------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29060120 | TASAJERA [29060120] |   10.9762 |   -74.3618 |         2 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Puebloviejo | 1965-08-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 504      |
| mean  |  30.9839 |
| std   |  60.6528 |
| min   |   0      |
| 25%   |   0      |
| 50%   |   6      |
| 75%   |  30      |
| max   | 485      |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_29060120_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060120_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060120_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060120_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: YE LA [15015020] (339 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.99241667,-74.21113889) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.99241667&lon=-74.21113889)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion   |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-----------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         15015020 | YE LA [15015020] |   10.9924 |   -74.2111 |        20 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Ciénaga     | 1967-07-15 00:00:00 | 2019-02-07 11:34:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 339      |
| mean  |  59.7829 |
| std   |  74.2829 |
| min   |   0      |
| 25%   |   0.5    |
| 50%   |  30.1    |
| 75%   |  85.2    |
| max   | 407      |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_15015020_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_15015020_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_15015020_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_15015020_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: CNO LA RAYA [16060010] (504 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=8.834722222,-72.79166667) or [Openstreet Map](https://www.openstreetmap.org/query?lat=8.834722222&lon=-72.79166667)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion         |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                          | Departamento       | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-----------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:---------------------------------------|:-------------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         16060010 | CNO LA RAYA [16060010] |   8.83472 |   -72.7917 |        75 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 08 - Santanderes-Arauca | Norte De Santander | Tibú        | 1973-04-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      53 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count |  504     |
| mean  |  304.344 |
| std   |  206.676 |
| min   |    0     |
| 25%   |  146.25  |
| 50%   |  284.5   |
| 75%   |  426.25  |
| max   | 1005     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_16060010_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_16060010_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_16060010_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_16060010_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: HACHARIRA [16070030] (309 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=8.875833333,-72.98222222) or [Openstreet Map](https://www.openstreetmap.org/query?lat=8.875833333&lon=-72.98222222)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                          | Departamento       | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:---------------------------------------|:-------------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         16070030 | HACHARIRA [16070030] |   8.87583 |   -72.9822 |        75 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 08 - Santanderes-Arauca | Norte De Santander | El Tarra    | 1973-04-15 00:00:00 | 2018-07-13 12:10:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |     200 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count |  309     |
| mean  |  390.891 |
| std   |  245.702 |
| min   |    0     |
| 25%   |  216     |
| 50%   |  359     |
| 75%   |  524     |
| max   | 1351     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_16070030_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_16070030_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_16070030_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_16070030_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: ORU [16070040] (472 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=8.641111111,-72.90944444) or [Openstreet Map](https://www.openstreetmap.org/query?lat=8.641111111&lon=-72.90944444)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion   |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                          | Departamento       | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-----------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:---------------------------------------|:-------------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         16070040 | ORU [16070040]   |   8.64111 |   -72.9094 |       150 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 08 - Santanderes-Arauca | Norte De Santander | Tibú        | 1973-04-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      67 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count |  472     |
| mean  |  353.798 |
| std   |  208.838 |
| min   |    8     |
| 25%   |  204.5   |
| 50%   |  341     |
| 75%   |  485.25  |
| max   | 1173     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_16070040_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_16070040_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_16070040_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_16070040_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: PALACIO EL [16050240] (327 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=8.610333333,-73.35113889) or [Openstreet Map](https://www.openstreetmap.org/query?lat=8.610333333&lon=-73.35113889)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion        |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                          | Departamento       | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:---------------------------------------|:-------------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1984-03-01 00:00:00 |         16050240 | PALACIO EL [16050240] |   8.61033 |   -73.3511 |      1280 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 08 - Santanderes-Arauca | Norte De Santander | Convención  | 1984-03-15 00:00:00 | 2014-08-28 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       3 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count |  327     |
| mean  |  178.577 |
| std   |  136.351 |
| min   |    0     |
| 25%   |   82     |
| 50%   |  156     |
| 75%   |  246     |
| max   | 1150     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_16050240_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_16050240_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_16050240_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_16050240_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: PISTA LA [16070020] (154 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.116666667,-72.86666667) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.116666667&lon=-72.86666667)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion      |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                          | Departamento       | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:--------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:---------------------------------------|:-------------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1986-03-01 00:00:00 |         16070020 | PISTA LA [16070020] |   9.11667 |   -72.8667 |        50 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 08 - Santanderes-Arauca | Norte De Santander | Tibú        | 1986-02-15 00:00:00 | 2019-01-21 08:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |     144 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count |  154     |
| mean  |  393.565 |
| std   |  269.214 |
| min   |    0     |
| 25%   |  162.25  |
| 50%   |  366     |
| 75%   |  557.5   |
| max   | 1210     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_16070020_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_16070020_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_16070020_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_16070020_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: PUERTO BARCO [16070010] (437 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=8.998055556,-72.89694444) or [Openstreet Map](https://www.openstreetmap.org/query?lat=8.998055556&lon=-72.89694444)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion          |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                          | Departamento       | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:---------------------------------------|:-------------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         16070010 | PUERTO BARCO [16070010] |   8.99806 |   -72.8969 |        50 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 08 - Santanderes-Arauca | Norte De Santander | Tibú        | 1973-04-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      50 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count |  437     |
| mean  |  410.432 |
| std   |  267.691 |
| min   |    0     |
| 25%   |  196     |
| 50%   |  396     |
| 75%   |  578     |
| max   | 1444     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_16070010_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_16070010_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_16070010_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_16070010_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: ASTREA [25020220] (503 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.492944444,-73.97288889) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.492944444&lon=-73.97288889)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion    |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25020220 | ASTREA [25020220] |   9.49294 |   -73.9729 |        50 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Astrea      | 1962-04-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 503     |
| mean  | 125.969 |
| std   | 101.616 |
| min   |   0     |
| 25%   |  43.3   |
| 50%   | 111.1   |
| 75%   | 189.85  |
| max   | 534     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_25020220_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020220_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020220_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020220_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: CANAL EL [25020240] (502 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.410472222,-73.89041667) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.410472222&lon=-73.89041667)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion      |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:--------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25020240 | CANAL EL [25020240] |   9.41047 |   -73.8904 |        70 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Chimichagua | 1963-03-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 502     |
| mean  | 136.406 |
| std   | 120.364 |
| min   |   0     |
| 25%   |  43     |
| 50%   | 112.5   |
| 75%   | 194     |
| max   | 735     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_25020240_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020240_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020240_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020240_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: CHIMICHAGUA [25021240] (504 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.260083333,-73.80986111) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.260083333&lon=-73.80986111)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion         |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-----------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25021240 | CHIMICHAGUA [25021240] |   9.26008 |   -73.8099 |       138 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Chimichagua | 1972-07-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 504     |
| mean  | 169.907 |
| std   | 147.9   |
| min   |   0     |
| 25%   |  46.875 |
| 50%   | 141.85  |
| 75%   | 265     |
| max   | 696.6   |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_25021240_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021240_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021240_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021240_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: CHIRIGUANA [25025250] (453 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.361027778,-73.59338889) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.361027778&lon=-73.59338889)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion        |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25025250 | CHIRIGUANA [25025250] |   9.36103 |   -73.5934 |        40 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Chiriguaná  | 1973-06-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |    28.7 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 453     |
| mean  | 135.746 |
| std   | 116.256 |
| min   |   0     |
| 25%   |  35     |
| 50%   | 115.4   |
| 75%   | 196.6   |
| max   | 549.9   |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_25025250_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25025250_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25025250_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25025250_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: CURUMANI D C [25021580] (188 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.183333333,-73.53333333) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.183333333&lon=-73.53333333)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion          |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1981-01-01 00:00:00 |         25021580 | CURUMANI D C [25021580] |   9.18333 |   -73.5333 |       100 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Curumaní    | 1979-11-15 00:00:00 | 1996-08-15 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       2 |       4 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 188     |
| mean  | 144.556 |
| std   | 116.792 |
| min   |   0     |
| 25%   |  52.75  |
| 50%   | 109.5   |
| 75%   | 217.75  |
| max   | 494     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_25021580_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021580_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021580_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021580_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: CURUMANI [25020250] (501 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.197194444,-73.54194444) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.197194444&lon=-73.54194444)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion      |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:--------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25020250 | CURUMANI [25020250] |   9.19719 |   -73.5419 |       100 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Curumaní    | 1963-03-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 501     |
| mean  | 142.694 |
| std   | 118.441 |
| min   |   0     |
| 25%   |  48     |
| 50%   | 117.9   |
| 75%   | 208.9   |
| max   | 644.3   |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_25020250_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020250_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020250_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020250_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: POPONTE [25020690] (504 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.423277778,-73.41094444) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.423277778&lon=-73.41094444)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion     |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25020690 | POPONTE [25020690] |   9.42328 |   -73.4109 |       500 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Curumaní    | 1972-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      60 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 504     |
| mean  | 153.358 |
| std   | 146.017 |
| min   |   0     |
| 25%   |  37     |
| 50%   | 112     |
| 75%   | 233.5   |
| max   | 753     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_25020690_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020690_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020690_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020690_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: PRIMAVERA LA [25020920] (418 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.216666667,-73.41666667) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.216666667&lon=-73.41666667)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion          |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25020920 | PRIMAVERA LA [25020920] |   9.21667 |   -73.4167 |       500 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Curumaní    | 1972-09-15 00:00:00 | 2019-02-07 11:35:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       5 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count |  418     |
| mean  |  139.157 |
| std   |  173.081 |
| min   |    0     |
| 25%   |   30     |
| 50%   |   88.5   |
| 75%   |  184.475 |
| max   | 1274     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_25020920_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020920_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020920_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020920_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: RINCONHONDO [25020260] (495 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.397027778,-73.48802778) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.397027778&lon=-73.48802778)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion         |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-----------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25020260 | RINCONHONDO [25020260] |   9.39703 |    -73.488 |       100 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Chiriguaná  | 1963-03-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      43 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count |  495     |
| mean  |  221.96  |
| std   |  172.012 |
| min   |    0     |
| 25%   |   89     |
| 50%   |  205     |
| 75%   |  318.5   |
| max   | 1163     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_25020260_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020260_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020260_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020260_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: SALOA [25020270] (500 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.193166667,-73.73130556) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.193166667&lon=-73.73130556)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion   |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-----------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25020270 | SALOA [25020270] |   9.19317 |   -73.7313 |        90 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Chimichagua | 1963-04-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      31 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 500     |
| mean  | 168.683 |
| std   | 144.303 |
| min   |   0     |
| 25%   |  48     |
| 50%   | 136     |
| 75%   | 262     |
| max   | 627     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_25020270_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020270_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020270_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020270_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: CENTENARIO HACIENDA [28025090] (500 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.85025,-73.26547222) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.85025&lon=-73.26547222)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion                 |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio       | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:----------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28025090 | CENTENARIO HACIENDA [28025090] |   9.85025 |   -73.2655 |       100 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Agustín Codazzi | 1976-12-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 500      |
| mean  | 123.833  |
| std   |  97.4444 |
| min   |   0      |
| 25%   |  45.3    |
| 50%   | 110.3    |
| 75%   | 187.725  |
| max   | 504.6    |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_28025090_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28025090_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28025090_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28025090_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: JAGUA LA [25020230] (482 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.562166667,-73.33947222) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.562166667&lon=-73.33947222)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion      |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio           | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:--------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:--------------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25020230 | JAGUA LA [25020230] |   9.56217 |   -73.3395 |       170 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | La Jagua De Ibirico | 1963-08-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       2 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 482     |
| mean  | 164.951 |
| std   | 141.109 |
| min   |   0     |
| 25%   |  56.225 |
| 50%   | 137     |
| 75%   | 241.5   |
| max   | 926     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_25020230_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020230_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020230_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020230_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: LLANOS LOS [28020230] (266 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.733333333,-73.3) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.733333333&lon=-73.3)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion        |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28020230 | LLANOS LOS [28020230] |   9.73333 |      -73.3 |       100 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Becerrill   | 1962-09-15 00:00:00 | 2010-10-15 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 266     |
| mean  | 125.781 |
| std   | 120.656 |
| min   |   0     |
| 25%   |  24.775 |
| 50%   | 110.1   |
| 75%   | 179.875 |
| max   | 675.7   |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_28020230_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020230_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020230_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020230_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: LOMA LA [25020280] (467 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.606527778,-73.61197222) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.606527778&lon=-73.61197222)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion     |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25020280 | LOMA LA [25020280] |   9.60653 |    -73.612 |        30 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | El Paso     | 1963-10-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 467     |
| mean  | 127.036 |
| std   | 118.767 |
| min   |   0     |
| 25%   |  35     |
| 50%   | 102     |
| 75%   | 185     |
| max   | 749     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_25020280_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020280_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020280_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020280_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: MOLINO EL [28040310] (357 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.776055556,-73.74341667) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.776055556&lon=-73.74341667)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28040310 | MOLINO EL [28040310] |   9.77606 |   -73.7434 |       110 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | El Paso     | 1972-08-15 00:00:00 | 2016-06-01 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 357     |
| mean  | 114.399 |
| std   |  94.932 |
| min   |   0     |
| 25%   |  40     |
| 50%   | 101     |
| 75%   | 165     |
| max   | 521     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_28040310_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040310_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040310_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040310_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: PASO EL   [28040350] (504 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.656972222,-73.74369444) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.656972222&lon=-73.74369444)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28040350 | PASO EL   [28040350] |   9.65697 |   -73.7437 |        30 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | El Paso     | 1972-08-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       4 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 504      |
| mean  | 110.536  |
| std   |  99.4701 |
| min   |   0      |
| 25%   |  31.8    |
| 50%   |  93.6    |
| 75%   | 160.8    |
| max   | 673.4    |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_28040350_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040350_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040350_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040350_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: PLAYAS LAS HACIENDA [28020080] (470 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.848083333,-73.46219444) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.848083333&lon=-73.46219444)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion                 |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio       | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:----------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28020080 | PLAYAS LAS HACIENDA [28020080] |   9.84808 |   -73.4622 |        60 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Agustín Codazzi | 1959-08-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 470     |
| mean  | 115.409 |
| std   | 105.649 |
| min   |   0     |
| 25%   |  30.25  |
| 50%   |  94     |
| 75%   | 172.5   |
| max   | 733     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_28020080_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020080_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020080_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020080_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: SAN GABRIEL [28020420] (448 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.844611111,-73.54769444) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.844611111&lon=-73.54769444)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion         |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-----------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28020420 | SAN GABRIEL [28020420] |   9.84461 |   -73.5477 |        70 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | San Diego   | 1972-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 448     |
| mean  | 122.556 |
| std   | 108.867 |
| min   |   0     |
| 25%   |  34.5   |
| 50%   | 102     |
| 75%   | 188     |
| max   | 567     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_28020420_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020420_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020420_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020420_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: SOCOMBA [28025080] (347 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.686666667,-73.24055556) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.686666667&lon=-73.24055556)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion     |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28025080 | SOCOMBA [28025080] |   9.68667 |   -73.2406 |       170 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Becerrill   | 1976-12-15 00:00:00 | 2019-02-07 11:41:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |    18.5 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 347      |
| mean  | 127.758  |
| std   |  98.1071 |
| min   |   0      |
| 25%   |  46.6    |
| 50%   | 113      |
| 75%   | 188.65   |
| max   | 496.9    |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_28025080_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28025080_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28025080_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28025080_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: YUCAL EL [25021650] (442 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.557388889,-73.87619444) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.557388889&lon=-73.87619444)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion      |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:--------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1984-12-01 00:00:00 |         25021650 | YUCAL EL [25021650] |   9.55739 |   -73.8762 |        40 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Astrea      | 1984-11-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 442     |
| mean  | 132.213 |
| std   | 129.695 |
| min   |   0     |
| 25%   |  32.25  |
| 50%   | 102.6   |
| 75%   | 198.5   |
| max   | 910     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_25021650_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021650_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021650_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021650_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: BOSCONIA [28040030] (499 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.97575,-73.88175) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.97575&lon=-73.88175)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion      |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:--------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28040030 | BOSCONIA [28040030] |   9.97575 |   -73.8817 |       130 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Bosconia    | 1979-11-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      30 |       4 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count |  499     |
| mean  |  116.19  |
| std   |  125.578 |
| min   |    0     |
| 25%   |   28     |
| 50%   |   90     |
| 75%   |  156.8   |
| max   | 1053     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_28040030_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040030_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040030_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040030_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: CODAZZI DC [28020460] (498 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.04463889,-73.24338889) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.04463889&lon=-73.24338889)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion        |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio       | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:----------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28020460 | CODAZZI DC [28020460] |   10.0446 |   -73.2434 |        90 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Agustín Codazzi | 1979-11-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |       4 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 498     |
| mean  | 128.521 |
| std   | 108.515 |
| min   |   0     |
| 25%   |  46.25  |
| 50%   | 104.5   |
| 75%   | 192.75  |
| max   | 591     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_28020460_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020460_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020460_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020460_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: ESPERANZA LA HACIENDA [28020150] (431 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.02997222,-73.66883333) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.02997222&lon=-73.66883333)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion                   |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1986-01-01 00:00:00 |         28020150 | ESPERANZA LA HACIENDA [28020150] |     10.03 |   -73.6688 |        60 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1961-05-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |       4 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 431      |
| mean  | 108.619  |
| std   |  88.2291 |
| min   |   0      |
| 25%   |  42      |
| 50%   |  89.2    |
| 75%   | 159      |
| max   | 518      |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_28020150_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020150_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020150_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020150_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: GUAYMARAL [28035040] (492 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.904916667,-73.64752778) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.904916667&lon=-73.64752778)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28035040 | GUAYMARAL [28035040] |   9.90492 |   -73.6475 |        50 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1972-08-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 492     |
| mean  | 107.14  |
| std   |  84.195 |
| min   |   0     |
| 25%   |  33.375 |
| 50%   |  97.45  |
| 75%   | 154.225 |
| max   | 425     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_28035040_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28035040_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28035040_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28035040_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: MANATURE HACIENDA [28040270] (484 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.03511111,-73.78852778) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.03511111&lon=-73.78852778)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion               |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-----------------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28040270 | MANATURE HACIENDA [28040270] |   10.0351 |   -73.7885 |       150 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Bosconia    | 1968-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 484      |
| mean  | 107.482  |
| std   |  89.9329 |
| min   |   0      |
| 25%   |  30      |
| 50%   |  98      |
| 75%   | 159      |
| max   | 560      |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_28040270_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040270_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040270_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040270_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: MOTILONIA CODAZZI [28025070] (504 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.00180556,-73.24938889) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.00180556&lon=-73.24938889)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion               |   Latitud |   Longitud |   Altitud | Categoria         | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio       | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-----------------------------|----------:|-----------:|----------:|:------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:----------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28025070 | MOTILONIA CODAZZI [28025070] |   10.0018 |   -73.2494 |       180 | Agrometeorológica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Agustín Codazzi | 1956-01-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 504     |
| mean  | 131.555 |
| std   | 104.05  |
| min   |   0     |
| 25%   |  47.95  |
| 50%   | 114.7   |
| 75%   | 194.45  |
| max   | 550.8   |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_28025070_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28025070_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28025070_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28025070_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: PALMARIGUANI [28040070] (494 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.930083333,-73.95488889) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.930083333&lon=-73.95488889)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion          |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28040070 | PALMARIGUANI [28040070] |   9.93008 |   -73.9549 |        80 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Bosconia    | 1963-01-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       5 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 494      |
| mean  | 111.56   |
| std   |  88.4919 |
| min   |   0      |
| 25%   |  40      |
| 50%   | 100      |
| 75%   | 165      |
| max   | 415      |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_28040070_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040070_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040070_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040070_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: PALMASOLA [28040400] (358 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.977416667,-73.88930556) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.977416667&lon=-73.88930556)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1984-06-01 00:00:00 |         28040400 | PALMASOLA [28040400] |   9.97742 |   -73.8893 |        50 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Bosconia    | 1984-06-15 00:00:00 | 2019-02-07 11:42:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |    86.2 |       4 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 358      |
| mean  | 103.43   |
| std   |  86.8242 |
| min   |   0      |
| 25%   |  34.25   |
| 50%   |  85      |
| 75%   | 148      |
| max   | 398      |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_28040400_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040400_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040400_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040400_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: RETORNO EL [28020600] (468 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.854722222,-73.35716667) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.854722222&lon=-73.35716667)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion        |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio       | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:----------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1981-12-01 00:00:00 |         28020600 | RETORNO EL [28020600] |   9.85472 |   -73.3572 |       150 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Agustín Codazzi | 1979-02-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      56 |       4 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 468     |
| mean  | 112.204 |
| std   |  97.752 |
| min   |   0     |
| 25%   |  33.75  |
| 50%   |  86     |
| 75%   | 172.85  |
| max   | 609     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_28020600_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020600_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020600_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020600_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: SANTA TERESA HACIENDA [28020440] (492 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.917027778,-73.28613889) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.917027778&lon=-73.28613889)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion                   |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio       | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:----------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28020440 | SANTA TERESA HACIENDA [28020440] |   9.91703 |   -73.2861 |        80 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Agustín Codazzi | 1959-04-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 492     |
| mean  | 127.331 |
| std   | 101.811 |
| min   |   0     |
| 25%   |  45     |
| 50%   | 109.4   |
| 75%   | 192     |
| max   | 610.6   |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_28020440_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020440_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020440_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020440_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: BOGOTANA LA [28020310] (281 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.1,-73.15) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.1&lon=-73.15)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion         |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio       | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-----------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:----------------|:--------------------|:--------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28020310 | BOGOTANA LA [28020310] |      10.1 |     -73.15 |       200 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Agustín Codazzi | 1968-09-15 00:00:00 | 2004-08-15 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       2 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 281     |
| mean  | 180.133 |
| std   | 148.914 |
| min   |   0     |
| 25%   |  63     |
| 50%   | 145     |
| 75%   | 261     |
| max   | 723     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_28020310_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020310_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020310_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020310_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: CARACOLI [28030190] (504 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.08869444,-73.73172222) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.08869444&lon=-73.73172222)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion      |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:--------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28030190 | CARACOLI [28030190] |   10.0887 |   -73.7317 |       220 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1972-07-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      14 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 504      |
| mean  |  93.3151 |
| std   |  86.66   |
| min   |   0      |
| 25%   |  14.475  |
| 50%   |  82.8    |
| 75%   | 144.55   |
| max   | 450.8    |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_28030190_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28030190_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28030190_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28030190_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: CHIMILAIMA [28040200] (187 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.06666667,-73.76666667) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.06666667&lon=-73.76666667)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion        |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28040200 | CHIMILAIMA [28040200] |   10.0667 |   -73.7667 |       120 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Bosconia    | 1962-08-15 00:00:00 | 1996-12-15 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 187      |
| mean  |  96.7465 |
| std   |  74.8121 |
| min   |   0      |
| 25%   |  33.5    |
| 50%   |  91      |
| 75%   | 146.5    |
| max   | 374      |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_28040200_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040200_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040200_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040200_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: LETICIA [28020590] (448 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.15238889,-73.22172222) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.15238889&lon=-73.22172222)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion     |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28020590 | LETICIA [28020590] |   10.1524 |   -73.2217 |       140 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | San Diego   | 1979-01-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      15 |       4 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 448      |
| mean  | 103.627  |
| std   |  91.3379 |
| min   |   0      |
| 25%   |  29      |
| 50%   |  83.3    |
| 75%   | 156      |
| max   | 542      |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_28020590_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020590_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020590_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020590_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: PARIS DE FRANCIA [28010370] (501 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.30708333,-73.32544444) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.30708333&lon=-73.32544444)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion              |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28010370 | PARIS DE FRANCIA [28010370] |   10.3071 |   -73.3254 |       180 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1971-11-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |       4 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 501     |
| mean  | 108.373 |
| std   |  94.421 |
| min   |   0     |
| 25%   |  26     |
| 50%   |  88     |
| 75%   | 171     |
| max   | 508     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_28010370_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010370_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010370_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010370_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: PAVAS LAS [28040060] (140 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.06666667,-73.88333333) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.06666667&lon=-73.88333333)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28040060 | PAVAS LAS [28040060] |   10.0667 |   -73.8833 |       150 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Bosconia    | 1963-01-15 00:00:00 | 1992-07-15 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      55 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 140     |
| mean  | 105.394 |
| std   |  98.432 |
| min   |   0     |
| 25%   |  30     |
| 50%   |  72.5   |
| 75%   | 152.75  |
| max   | 500     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_28040060_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040060_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040060_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040060_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: RINCON EL [28025020] (494 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.27138889,-73.13138889) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.27138889&lon=-73.13138889)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28025020 | RINCON EL [28025020] |   10.2714 |   -73.1314 |       350 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | San Diego   | 1964-02-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |     9.6 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 494      |
| mean  | 110.783  |
| std   |  82.2089 |
| min   |   0      |
| 25%   |  42.025  |
| 50%   | 104.8    |
| 75%   | 165.05   |
| max   | 421.2    |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_28025020_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28025020_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28025020_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28025020_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: SAN BENITO [28020410] (457 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.18416667,-73.31702778) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.18416667&lon=-73.31702778)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion        |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28020410 | SAN BENITO [28020410] |   10.1842 |    -73.317 |       150 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | San Diego   | 1972-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 457     |
| mean  | 107.139 |
| std   | 101.903 |
| min   |   0     |
| 25%   |  27.9   |
| 50%   |  82     |
| 75%   | 156     |
| max   | 757     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_28020410_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020410_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020410_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020410_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: VILLA MARLENE [28010070] (432 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.1855,-73.46711111) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.1855&lon=-73.46711111)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion           |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1986-01-01 00:00:00 |         28010070 | VILLA MARLENE [28010070] |   10.1855 |   -73.4671 |       120 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1987-01-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |       4 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 432     |
| mean  | 116.327 |
| std   | 106.916 |
| min   |   0     |
| 25%   |  32.75  |
| 50%   |  98.3   |
| 75%   | 179.75  |
| max   | 581     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_28010070_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010070_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010070_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010070_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: VILLA ROSA [28035010] (462 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.19066667,-73.54738889) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.19066667&lon=-73.54738889)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion        |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28035010 | VILLA ROSA [28035010] |   10.1907 |   -73.5474 |        70 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1968-03-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |       4 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 462     |
| mean  | 110.852 |
| std   |  91.875 |
| min   |   0     |
| 25%   |  30.25  |
| 50%   |  95.75  |
| 75%   | 168.375 |
| max   | 479.6   |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_28035010_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28035010_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28035010_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28035010_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: ATANQUEZ [28010360] (470 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.69733333,-73.35305556) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.69733333&lon=-73.35305556)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion      |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:--------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28010360 | ATANQUEZ [28010360] |   10.6973 |   -73.3531 |       800 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1959-04-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count |  470     |
| mean  |  172.4   |
| std   |  212.311 |
| min   |    0     |
| 25%   |   20     |
| 50%   |  102.05  |
| 75%   |  252.425 |
| max   | 1647.3   |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_28010360_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010360_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010360_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010360_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: CALLAO EL [28035020] (474 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.36305556,-73.31944444) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.36305556&lon=-73.31944444)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28035020 | CALLAO EL [28035020] |   10.3631 |   -73.3194 |       110 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1968-03-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |       4 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 474      |
| mean  |  98.4741 |
| std   |  84.522  |
| min   |   0      |
| 25%   |  21.025  |
| 50%   |  85.35   |
| 75%   | 152.45   |
| max   | 464.2    |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_28035020_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28035020_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28035020_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28035020_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: CUEVAS LAS [28040170] (106 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.46666667,-73.56666667) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.46666667&lon=-73.56666667)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion        |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio    | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:-------------|:--------------------|:--------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28040170 | CUEVAS LAS [28040170] |   10.4667 |   -73.5667 |      1260 | Pluviográfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Pueblo Bello | 1963-06-15 00:00:00 | 1996-02-15 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      63 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 106     |
| mean  | 115.199 |
| std   | 121.212 |
| min   |   0     |
| 25%   |  18.15  |
| 50%   |  60.5   |
| 75%   | 200.25  |
| max   | 505     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_28040170_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040170_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040170_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040170_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: DESCANSO EL [28010020] (359 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.48011111,-73.23719444) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.48011111&lon=-73.23719444)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion         |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-----------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1986-01-01 00:00:00 |         28010020 | DESCANSO EL [28010020] |   10.4801 |   -73.2372 |       160 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1986-04-15 00:00:00 | 2019-02-07 11:41:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |       4 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 359      |
| mean  |  78.6925 |
| std   |  88.7822 |
| min   |   0      |
| 25%   |  10      |
| 50%   |  55      |
| 75%   | 125      |
| max   | 713      |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_28010020_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010020_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010020_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010020_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: MANAURE [28010040] (498 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.39138889,-73.02527778) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.39138889&lon=-73.02527778)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion     |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio                | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:-------------------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28010040 | MANAURE [28010040] |   10.3914 |   -73.0253 |       740 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Manaure Balcón Del Cesar | 1975-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       7 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 498     |
| mean  | 151.934 |
| std   | 128.693 |
| min   |   0     |
| 25%   |  48.325 |
| 50%   | 130.1   |
| 75%   | 220.625 |
| max   | 748.7   |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_28010040_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010040_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010040_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010040_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: PUEBLO BELLO [28040010] (504 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.41463889,-73.58502778) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.41463889&lon=-73.58502778)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion          |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio    | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:-------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28040010 | PUEBLO BELLO [28040010] |   10.4146 |    -73.585 |        10 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Pueblo Bello | 1963-01-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count |  504     |
| mean  |  178.377 |
| std   |  153.483 |
| min   |    0     |
| 25%   |   53.75  |
| 50%   |  157.5   |
| 75%   |  261.25  |
| max   | 1193     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_28040010_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040010_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040010_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040010_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: SAN ANGEL [28030220] (401 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.34705556,-73.44413889) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.34705556&lon=-73.44413889)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1983-07-01 00:00:00 |         28030220 | SAN ANGEL [28030220] |   10.3471 |   -73.4441 |       244 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1983-06-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      79 |       4 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 401      |
| mean  |  85.2723 |
| std   |  91.6286 |
| min   |   0      |
| 25%   |   1.3    |
| 50%   |  58.3    |
| 75%   | 135      |
| max   | 525      |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_28030220_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28030220_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28030220_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28030220_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: SAN JOSE D ORIENTE [28025040] (171 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.35,-73.05) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.35&lon=-73.05)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion                |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28025040 | SAN JOSE D ORIENTE [28025040] |     10.35 |     -73.05 |       850 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | La Paz      | 1975-08-15 00:00:00 | 1998-05-15 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |     3.7 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 171      |
| mean  |  96.6094 |
| std   |  90.3915 |
| min   |   0      |
| 25%   |  26.1    |
| 50%   |  68.8    |
| 75%   | 143.5    |
| max   | 360.6    |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_28025040_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28025040_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28025040_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28025040_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: SAN SEBASTIAN DE [29060090] (501 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.56330556,-73.60380556) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.56330556&lon=-73.60380556)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion              |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio    | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:-------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29060090 | SAN SEBASTIAN DE [29060090] |   10.5633 |   -73.6038 |        20 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Pueblo Bello | 1968-05-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      11 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 501     |
| mean  | 109.604 |
| std   |  77.811 |
| min   |   0     |
| 25%   |  42     |
| 50%   | 106     |
| 75%   | 168     |
| max   | 382     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_29060090_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060090_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060090_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060090_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: VILLA CARMELITA [28010140] (255 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.53333333,-73.3) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.53333333&lon=-73.3)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion             |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28010140 | VILLA CARMELITA [28010140] |   10.5333 |      -73.3 |       450 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1968-09-15 00:00:00 | 2004-08-15 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       3 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 255     |
| mean  | 131.152 |
| std   | 134.891 |
| min   |   0     |
| 25%   |  24     |
| 50%   |  89     |
| 75%   | 194     |
| max   | 630     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_28010140_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010140_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010140_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010140_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: PATILLAL [28010090] (474 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.70386111,-73.21161111) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.70386111&lon=-73.21161111)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion      |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:--------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28010090 | PATILLAL [28010090] |   10.7039 |   -73.2116 |       450 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1962-12-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 474      |
| mean  |  92.6331 |
| std   |  95.1618 |
| min   |   0      |
| 25%   |  10      |
| 50%   |  71.5    |
| 75%   | 138      |
| max   | 631      |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_28010090_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010090_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010090_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010090_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: PUEBLO BELLO  [28045010] (228 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.37,-73.63) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.37&lon=-73.63)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion           |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                          | AreaOperativa                               | Departamento   | Municipio    | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------------|----------:|-----------:|----------:|:--------------------|:---------------------------------|:--------------------------------------------|:---------------|:-------------|:--------------------|:--------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28045010 | PUEBLO BELLO  [28045010] |     10.37 |     -73.63 |      1000 | Climática Ordinaria | FEDERACION NACIONAL DE CAFETEROS | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Pueblo Bello | 1954-02-15 00:00:00 | 2020-10-21 17:13:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |    47.7 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 228     |
| mean  | 129.799 |
| std   | 131.563 |
| min   |   0     |
| 25%   |   0     |
| 50%   |  93.3   |
| 75%   | 224.7   |
| max   | 502.1   |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_28045010_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28045010_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28045010_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28045010_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: SARACHUI [28010130] (122 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.78333333,-73.4) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.78333333&lon=-73.4)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion      |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:--------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28010130 | SARACHUI [28010130] |   10.7833 |      -73.4 |      1560 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1968-04-15 00:00:00 | 1990-05-15 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      27 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count |  122     |
| mean  |  230.704 |
| std   |  218.823 |
| min   |    0     |
| 25%   |   60     |
| 50%   |  162     |
| 75%   |  342.25  |
| max   | 1009     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_28010130_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010130_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010130_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010130_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: CANAVERALES [15060080] (503 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.75777778,-72.84522222) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.75777778&lon=-72.84522222)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion         |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio          | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-----------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:-------------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         15060080 | CANAVERALES [15060080] |   10.7578 |   -72.8452 |       230 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | San Juan Del Cesar | 1963-08-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 503      |
| mean  |  98.771  |
| std   |  93.6652 |
| min   |   0      |
| 25%   |  15      |
| 50%   |  83      |
| 75%   | 148.5    |
| max   | 722      |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_15060080_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_15060080_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_15060080_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_15060080_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: CONEJO EL [15060150] (504 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.77794444,-72.79819444) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.77794444&lon=-72.79819444)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         15060150 | CONEJO EL [15060150] |   10.7779 |   -72.7982 |       350 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | Fonseca     | 1975-10-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 504      |
| mean  |  72.1262 |
| std   |  80.4786 |
| min   |   0      |
| 25%   |   8      |
| 50%   |  46.1    |
| 75%   | 107.375  |
| max   | 383      |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_15060150_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_15060150_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_15060150_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_15060150_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: HATICO D LOS INDIO [28010200] (471 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.86022222,-73.11416667) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.86022222&lon=-73.11416667)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion                |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio          | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:-------------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28010200 | HATICO D LOS INDIO [28010200] |   10.8602 |   -73.1142 |       594 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | San Juan Del Cesar | 1970-01-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 471      |
| mean  |  82.41   |
| std   |  90.3403 |
| min   |   0      |
| 25%   |   5.4    |
| 50%   |  52      |
| 75%   | 129.4    |
| max   | 556      |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_28010200_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010200_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010200_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010200_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: JUGUETE EL [15060070] (387 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.786,-72.76836111) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.786&lon=-72.76836111)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion        |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         15060070 | JUGUETE EL [15060070] |    10.786 |   -72.7684 |       390 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | Fonseca     | 1971-05-15 00:00:00 | 2014-08-28 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 387     |
| mean  | 103.287 |
| std   | 105.964 |
| min   |   0     |
| 25%   |  15     |
| 50%   |  82     |
| 75%   | 150     |
| max   | 655     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_15060070_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_15060070_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_15060070_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_15060070_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: LA PAULINA - AUT [15065040] (243 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.89813889,-72.82847222) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.89813889&lon=-72.82847222)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion              |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-04-01 00:00:00 |         15065040 | LA PAULINA - AUT [15065040] |   10.8981 |   -72.8285 |       170 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | Fonseca     | 1966-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |    72.3 |       4 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 243      |
| mean  |  65.5008 |
| std   |  59.54   |
| min   |   0      |
| 25%   |  10.8    |
| 50%   |  53      |
| 75%   | 107.75   |
| max   | 237.7    |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_15065040_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_15065040_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_15065040_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_15065040_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: PAMPLONA [28010280] (15 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.65,-72.85) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.65&lon=-72.85)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion      |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio          | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:--------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:-------------------|:--------------------|:--------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28010280 | PAMPLONA [28010280] |     10.65 |     -72.85 |       690 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | San Juan Del Cesar | 1971-05-15 00:00:00 | 1993-11-15 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       2 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count |  15      |
| mean  |  52.2667 |
| std   |  55.7577 |
| min   |   2      |
| 25%   |  12.5    |
| 50%   |  26      |
| 75%   |  77      |
| max   | 169      |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_28010280_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010280_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010280_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010280_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: SABANAS DE MANUELA [15060050] (487 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.953,-73.04797222) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.953&lon=-73.04797222)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion                |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         15060050 | SABANAS DE MANUELA [15060050] |    10.953 |    -73.048 |       420 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | Distracción | 1963-08-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 487      |
| mean  |  87.9507 |
| std   |  83.7311 |
| min   |   0      |
| 25%   |  12.1    |
| 50%   |  74      |
| 75%   | 138.1    |
| max   | 489.2    |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_15060050_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_15060050_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_15060050_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_15060050_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: URUMITA [28015070] (499 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.56638889,-73.01638889) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.56638889&lon=-73.01638889)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion     |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28015070 | URUMITA [28015070] |   10.5664 |   -73.0164 |       255 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | Urumita     | 1975-08-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 499      |
| mean  |  98.0299 |
| std   |  84.267  |
| min   |   0      |
| 25%   |  28.35   |
| 50%   |  87.9    |
| 75%   | 150.7    |
| max   | 456.1    |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_28015070_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28015070_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28015070_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28015070_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: VILLANUEVA [28010340] (492 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.61583333,-72.98194444) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.61583333&lon=-72.98194444)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion        |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28010340 | VILLANUEVA [28010340] |   10.6158 |   -72.9819 |       340 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | Villanueva  | 1970-08-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 492      |
| mean  |  99.5524 |
| std   |  92.5377 |
| min   |   0      |
| 25%   |  16.975  |
| 50%   |  82.5    |
| 75%   | 154      |
| max   | 457      |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_28010340_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010340_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010340_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010340_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: AEROPUERTO LAS FLORES [25025090] (466 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.046333333,-73.97083333) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.046333333&lon=-73.97083333)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion                   |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25025090 | AEROPUERTO LAS FLORES [25025090] |   9.04633 |   -73.9708 |        34 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | El Banco    | 1952-02-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      70 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 466     |
| mean  | 164.917 |
| std   | 134.386 |
| min   |   0     |
| 25%   |  53.3   |
| 50%   | 139.15  |
| 75%   | 246.2   |
| max   | 609.3   |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_25025090_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25025090_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25025090_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25025090_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: BRILLANTE EL [28040320] (487 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.70275,-73.95913889) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.70275&lon=-73.95913889)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion          |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28040320 | BRILLANTE EL [28040320] |   9.70275 |   -73.9591 |       135 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Santa Ana   | 1972-07-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       7 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 487      |
| mean  | 124.416  |
| std   |  96.7825 |
| min   |   0      |
| 25%   |  50.5    |
| 50%   | 107      |
| 75%   | 172.5    |
| max   | 491      |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_28040320_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040320_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040320_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040320_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: IRAN [25021620] (468 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.683777778,-74.32216667) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.683777778&lon=-74.32216667)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion   |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio     | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-----------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:--------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1982-07-01 00:00:00 |         25021620 | IRAN [25021620]  |   9.68378 |   -74.3222 |        80 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Nueva Granada | 1982-06-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      63 |       4 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 468     |
| mean  | 116.16  |
| std   |  92.907 |
| min   |   0     |
| 25%   |  44.75  |
| 50%   | 101.5   |
| 75%   | 161     |
| max   | 716     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_25021620_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021620_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021620_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021620_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: MENCHIQUEJO [25021040] (503 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.188055556,-74.04422222) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.188055556&lon=-74.04422222)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion         |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-----------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25021040 | MENCHIQUEJO [25021040] |   9.18806 |   -74.0442 |        25 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | El Banco    | 1974-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 503     |
| mean  | 161.868 |
| std   | 139.083 |
| min   |   0     |
| 25%   |  45     |
| 50%   | 139     |
| 75%   | 245.5   |
| max   | 739     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_25021040_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021040_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021040_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021040_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: NEGRITOS LOS [25021200] (484 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.026666667,-74.07944444) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.026666667&lon=-74.07944444)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion          |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25021200 | NEGRITOS LOS [25021200] |   9.02667 |   -74.0794 |        26 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena      | El Banco    | 1976-07-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      21 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 484     |
| mean  | 190.166 |
| std   | 168.025 |
| min   |   0     |
| 25%   |  50     |
| 50%   | 149     |
| 75%   | 284.5   |
| max   | 934     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_25021200_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021200_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021200_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021200_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: PUEBLITO EL [25021500] (492 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.581166667,-74.35225) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.581166667&lon=-74.35225)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion         |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-----------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25021500 | PUEBLITO EL [25021500] |   9.58117 |   -74.3522 |        35 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Santa Ana   | 1976-10-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       4 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 492      |
| mean  |  99.214  |
| std   |  74.7592 |
| min   |   0      |
| 25%   |  41      |
| 50%   |  88      |
| 75%   | 145      |
| max   | 368      |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_25021500_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021500_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021500_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021500_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: SAN ROQUE ALERTAS [25021380] (477 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.07,-74.15) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.07&lon=-74.15)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion               |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-----------------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-06-01 00:00:00 |         25021380 | SAN ROQUE ALERTAS [25021380] |      9.07 |     -74.15 |        24 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena      | El Banco    | 1980-05-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |     231 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 477     |
| mean  | 167.207 |
| std   | 139.418 |
| min   |   0     |
| 25%   |  53     |
| 50%   | 140     |
| 75%   | 257     |
| max   | 724     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_25021380_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021380_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021380_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021380_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: SAN SEBASTIAN [25020900] (492 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.233888889,-74.35583333) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.233888889&lon=-74.35583333)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion           |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio                   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:----------------------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25020900 | SAN SEBASTIAN [25020900] |   9.23389 |   -74.3558 |        65 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena      | San Sebastián De Buenavista | 1974-01-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 492     |
| mean  | 131.34  |
| std   | 114.881 |
| min   |   0     |
| 25%   |  30     |
| 50%   | 106     |
| 75%   | 207     |
| max   | 510     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_25020900_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020900_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020900_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020900_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: SEIS EL [25025300] (470 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.683666667,-74.32227778) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.683666667&lon=-74.32227778)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion     |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio                   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:----------------------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25025300 | SEIS EL [25025300] |   9.68367 |   -74.3223 |        50 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | San Sebastián De Buenavista | 1984-11-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 470      |
| mean  | 110.96   |
| std   |  92.9367 |
| min   |   0      |
| 25%   |  35.225  |
| 50%   |  90.9    |
| 75%   | 163.8    |
| max   | 459.2    |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_25025300_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25025300_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25025300_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25025300_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: VILLA CONCEPCION [28040300] (480 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.706305556,-73.85944444) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.706305556&lon=-73.85944444)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion              |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio             | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:----------------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28040300 | VILLA CONCEPCION [28040300] |   9.70631 |   -73.8594 |       120 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Ariguaní (El Dificil) | 1972-07-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 480      |
| mean  | 114.796  |
| std   |  97.6011 |
| min   |   0      |
| 25%   |  39      |
| 50%   |  96      |
| 75%   | 162      |
| max   | 564      |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_28040300_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040300_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040300_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040300_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: AGUADAS LAS ALERTA [25021540] (490 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=8.949997222,-74.049997222) or [Openstreet Map](https://www.openstreetmap.org/query?lat=8.949997222&lon=-74.049997222)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion                |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio          | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:-------------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25021540 | AGUADAS LAS ALERTA [25021540] |      8.95 |     -74.05 |        30 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | San Martín De Loba | 1978-11-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 490     |
| mean  | 178.49  |
| std   | 144.689 |
| min   |   0     |
| 25%   |  66.25  |
| 50%   | 144.5   |
| 75%   | 264.925 |
| max   | 721     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_25021540_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021540_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021540_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021540_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: BARRANCO DE LOBA [25020880] (490 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=8.946666667,-74.11055556) or [Openstreet Map](https://www.openstreetmap.org/query?lat=8.946666667&lon=-74.11055556)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion              |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio        | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:-----------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25020880 | BARRANCO DE LOBA [25020880] |   8.94667 |   -74.1106 |        25 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | Barranco De Loba | 1974-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |       4 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 490     |
| mean  | 193.8   |
| std   | 160.698 |
| min   |   0     |
| 25%   |  60     |
| 50%   | 163.5   |
| 75%   | 291     |
| max   | 764     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_25020880_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020880_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020880_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020880_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: CHILLOA [25020890] (483 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.119388889,-74.22194444) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.119388889&lon=-74.22194444)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion     |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25020890 | CHILLOA [25020890] |   9.11939 |   -74.2219 |        20 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | Margarita   | 1974-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      15 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 483     |
| mean  | 155.821 |
| std   | 128.157 |
| min   |   0     |
| 25%   |  49     |
| 50%   | 130     |
| 75%   | 244     |
| max   | 593     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_25020890_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020890_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020890_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020890_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: SUDAN EL [25021320] (491 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=8.643333333,-74.21222222) or [Openstreet Map](https://www.openstreetmap.org/query?lat=8.643333333&lon=-74.21222222)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion      |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio              | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:--------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:-----------------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25021320 | SUDAN EL [25021320] |   8.64333 |   -74.2122 |        23 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | Tiquisio (Puerto Rico) | 1976-10-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |    20.9 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 491     |
| mean  | 160.853 |
| std   | 141.005 |
| min   |   0     |
| 25%   |  48     |
| 50%   | 133     |
| 75%   | 240     |
| max   | 744     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_25021320_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021320_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021320_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021320_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: PLAYITAS [25020870] (497 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=8.822777778,-73.96583333) or [Openstreet Map](https://www.openstreetmap.org/query?lat=8.822777778&lon=-73.96583333)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion      |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio          | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:--------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:-------------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25020870 | PLAYITAS [25020870] |   8.82278 |   -73.9658 |        40 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | San Martín De Loba | 1974-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      12 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 497     |
| mean  | 155.739 |
| std   | 135.675 |
| min   |   0     |
| 25%   |  45     |
| 50%   | 136     |
| 75%   | 233     |
| max   | 835     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_25020870_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020870_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020870_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020870_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: SANTA ROSA [25021090] (475 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.093333333,-74.31388889) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.093333333&lon=-74.31388889)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion        |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio    | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:-------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25021090 | SANTA ROSA [25021090] |   9.09333 |   -74.3139 |        40 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | San Fernando | 1974-10-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       5 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 475     |
| mean  | 157.96  |
| std   | 141.425 |
| min   |   0     |
| 25%   |  40     |
| 50%   | 125     |
| 75%   | 240.9   |
| max   | 680     |

</div>


![R.LTWB](Graph/Plot_PTPM_TT_M_25021090_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021090_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021090_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021090_DensityKDE.png)


### Analysis from 1980 to 2021 for Etiqueta == "TMX_CON": 185849 (36.09%)

Pivot table: [Pivot_TMX_CON.csv](Pivot_TMX_CON.csv)
![R.LTWB](Graph/Plot_TMX_CON_TimeSerie.png)
![R.LTWB](Graph/Plot_TMX_CON_DensityKDE.png)

<div align="center">



**TMX_CON - Station: ALGARROBO [28045020] (1050 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.15,-74.06666667) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.15&lon=-74.06666667)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1983-01-01 00:00:00 |         28045020 | ALGARROBO [28045020] |     10.15 |   -74.0667 |        60 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | El Copey    | 1964-02-15 00:00:00 | 1987-04-15 00:00:00 | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |      36 |      50 |           nan |              1200 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |      Valor |
|:------|-----------:|
| count | 1050       |
| mean  |   33.8226  |
| std   |    2.13222 |
| min   |   27.2     |
| 25%   |   32.25    |
| 50%   |   33.8     |
| 75%   |   35.4     |
| max   |   39.2     |

</div>


![R.LTWB](Graph/Plot_TMX_CON_28045020_TimeSerie.png)
![R.LTWB](Graph/Plot_TMX_CON_28045020_Boxplot.png)
![R.LTWB](Graph/Plot_TMX_CON_28045020_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_28045020_DensityKDE.png)

<div align="center">



**TMX_CON - Station: CENTENARIO HACIENDA [28025090] (12953 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.85025,-73.26547222) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.85025&lon=-73.26547222)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion                 |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio       | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:----------------|:--------------------|:------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1981-01-03 00:00:00 |         28025090 | CENTENARIO HACIENDA [28025090] |   9.85025 |   -73.2655 |       100 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Agustín Codazzi | 1976-12-15 00:00:00 | NaT               | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    32.6 |      50 |           nan |              1200 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |       Valor |
|:------|------------:|
| count | 12953       |
| mean  |    34.3336  |
| std   |     2.09333 |
| min   |    23.8     |
| 25%   |    33       |
| 50%   |    34.4     |
| 75%   |    35.8     |
| max   |    42.3     |

</div>


![R.LTWB](Graph/Plot_TMX_CON_28025090_TimeSerie.png)
![R.LTWB](Graph/Plot_TMX_CON_28025090_Boxplot.png)
![R.LTWB](Graph/Plot_TMX_CON_28025090_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_28025090_DensityKDE.png)

<div align="center">



**TMX_CON - Station: CHIRIGUANA [25025250] (11758 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.361027778,-73.59338889) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.361027778&lon=-73.59338889)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion        |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1981-04-01 00:00:00 |         25025250 | CHIRIGUANA [25025250] |   9.36103 |   -73.5934 |        40 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Chiriguaná  | 1973-06-15 00:00:00 | NaT               | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    37.6 |      50 |           nan |              1200 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |       Valor |
|:------|------------:|
| count | 11758       |
| mean  |    33.787   |
| std   |     2.07519 |
| min   |    26.6     |
| 25%   |    32.4     |
| 50%   |    34       |
| 75%   |    35       |
| max   |    42.6     |

</div>


![R.LTWB](Graph/Plot_TMX_CON_25025250_TimeSerie.png)
![R.LTWB](Graph/Plot_TMX_CON_25025250_Boxplot.png)
![R.LTWB](Graph/Plot_TMX_CON_25025250_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_25025250_DensityKDE.png)

<div align="center">



**TMX_CON - Station: COLEGIO AGROPECUARIO PAILITAS  - AUT [25025330] (7606 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=8.954222222,-73.63008333) or [Openstreet Map](https://www.openstreetmap.org/query?lat=8.954222222&lon=-73.63008333)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion                                  |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------------------------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1990-03-27 00:00:00 |         25025330 | COLEGIO AGROPECUARIO PAILITAS  - AUT [25025330] |   8.95422 |   -73.6301 |        50 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Pailitas    | 1987-09-15 00:00:00 | NaT               | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    34.2 |      50 |           nan |              1200 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |     Valor |
|:------|----------:|
| count | 7606      |
| mean  |   33.2243 |
| std   |    2.0554 |
| min   |   23.2    |
| 25%   |   31.8    |
| 50%   |   33      |
| 75%   |   34.6    |
| max   |   41.6    |

</div>


![R.LTWB](Graph/Plot_TMX_CON_25025330_TimeSerie.png)
![R.LTWB](Graph/Plot_TMX_CON_25025330_Boxplot.png)
![R.LTWB](Graph/Plot_TMX_CON_25025330_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_25025330_DensityKDE.png)

<div align="center">



**TMX_CON - Station: GUAIRA LA HACIENDA [28045040] (784 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.616666667,-73.8) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.616666667&lon=-73.8)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion                |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1987-09-10 00:00:00 |         28045040 | GUAIRA LA HACIENDA [28045040] |   9.61667 |      -73.8 |        50 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | El Paso     | 1987-09-15 00:00:00 | 1994-07-15 00:00:00 | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    32.4 |      50 |           nan |              1200 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |     Valor |
|:------|----------:|
| count | 784       |
| mean  |  34.5605  |
| std   |   2.25236 |
| min   |  26       |
| 25%   |  33       |
| 50%   |  34.6     |
| 75%   |  36       |
| max   |  41.8     |

</div>


![R.LTWB](Graph/Plot_TMX_CON_28045040_TimeSerie.png)
![R.LTWB](Graph/Plot_TMX_CON_28045040_Boxplot.png)
![R.LTWB](Graph/Plot_TMX_CON_28045040_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_28045040_DensityKDE.png)

<div align="center">



**TMX_CON - Station: GUAYMARAL [28035040] (9424 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.904916667,-73.64752778) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.904916667&lon=-73.64752778)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1981-06-01 00:00:00 |         28035040 | GUAYMARAL [28035040] |   9.90492 |   -73.6475 |        50 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1972-08-15 00:00:00 | NaT               | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    35.2 |      50 |           nan |              1200 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |      Valor |
|:------|-----------:|
| count | 9424       |
| mean  |   36.1116  |
| std   |    2.03179 |
| min   |   26       |
| 25%   |   35       |
| 50%   |   36.4     |
| 75%   |   37.4     |
| max   |   42.4     |

</div>


![R.LTWB](Graph/Plot_TMX_CON_28035040_TimeSerie.png)
![R.LTWB](Graph/Plot_TMX_CON_28035040_Boxplot.png)
![R.LTWB](Graph/Plot_TMX_CON_28035040_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_28035040_DensityKDE.png)

<div align="center">



**TMX_CON - Station: LA GLORIA [23215060] (960 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=8.615277778,-73.800555556) or [Openstreet Map](https://www.openstreetmap.org/query?lat=8.615277778&lon=-73.800555556)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                          | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:---------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1983-09-17 00:00:00 |         23215060 | LA GLORIA [23215060] |   8.61528 |   -73.8006 |        35 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 08 - Santanderes-Arauca | Cesar          | La Gloria   | 1995-05-15 00:00:00 | 2018-06-19 10:35:00 | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |      33 |      50 |           nan |              1200 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |     Valor |
|:------|----------:|
| count | 960       |
| mean  |  32.7978  |
| std   |   1.77501 |
| min   |  27       |
| 25%   |  31.6     |
| 50%   |  32.8     |
| 75%   |  34       |
| max   |  37.4     |

</div>


![R.LTWB](Graph/Plot_TMX_CON_23215060_TimeSerie.png)
![R.LTWB](Graph/Plot_TMX_CON_23215060_Boxplot.png)
![R.LTWB](Graph/Plot_TMX_CON_23215060_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_23215060_DensityKDE.png)

<div align="center">



**TMX_CON - Station: MOTILONIA CODAZZI [28025070] (13398 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.00180556,-73.24938889) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.00180556&lon=-73.24938889)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion               |   Latitud |   Longitud |   Altitud | Categoria         | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio       | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-----------------------------|----------:|-----------:|----------:|:------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:----------------|:--------------------|:------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28025070 | MOTILONIA CODAZZI [28025070] |   10.0018 |   -73.2494 |       180 | Agrometeorológica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Agustín Codazzi | 1956-01-15 00:00:00 | NaT               | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    34.8 |      50 |           nan |              1200 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |       Valor |
|:------|------------:|
| count | 13398       |
| mean  |    34.4325  |
| std   |     2.35604 |
| min   |    24.1     |
| 25%   |    32.8     |
| 50%   |    34.4     |
| 75%   |    36.2     |
| max   |    42.8     |

</div>


![R.LTWB](Graph/Plot_TMX_CON_28025070_TimeSerie.png)
![R.LTWB](Graph/Plot_TMX_CON_28025070_Boxplot.png)
![R.LTWB](Graph/Plot_TMX_CON_28025070_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_28025070_DensityKDE.png)

<div align="center">



**TMX_CON - Station: SOCOMBA [28025080] (7076 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.686666667,-73.24055556) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.686666667&lon=-73.24055556)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion     |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-03 00:00:00 |         28025080 | SOCOMBA [28025080] |   9.68667 |   -73.2406 |       170 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Becerrill   | 1976-12-15 00:00:00 | 2019-02-07 11:41:00 | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |      35 |      50 |           nan |              1200 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |      Valor |
|:------|-----------:|
| count | 7076       |
| mean  |   33.5969  |
| std   |    2.05285 |
| min   |   26.4     |
| 25%   |   32.2     |
| 50%   |   33.6     |
| 75%   |   35       |
| max   |   40       |

</div>


![R.LTWB](Graph/Plot_TMX_CON_28025080_TimeSerie.png)
![R.LTWB](Graph/Plot_TMX_CON_28025080_Boxplot.png)
![R.LTWB](Graph/Plot_TMX_CON_28025080_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_28025080_DensityKDE.png)

<div align="center">



**TMX_CON - Station: VILLA ROSA [28035010] (8442 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.19066667,-73.54738889) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.19066667&lon=-73.54738889)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion        |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-11 00:00:00 |         28035010 | VILLA ROSA [28035010] |   10.1907 |   -73.5474 |        70 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1968-03-15 00:00:00 | NaT               | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    35.2 |      50 |           nan |              1200 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |      Valor |
|:------|-----------:|
| count | 8442       |
| mean  |   35.0506  |
| std   |    2.25909 |
| min   |   25       |
| 25%   |   33.6     |
| 50%   |   35.2     |
| 75%   |   36.6     |
| max   |   42.4     |

</div>


![R.LTWB](Graph/Plot_TMX_CON_28035010_TimeSerie.png)
![R.LTWB](Graph/Plot_TMX_CON_28035010_Boxplot.png)
![R.LTWB](Graph/Plot_TMX_CON_28035010_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_28035010_DensityKDE.png)

<div align="center">



**TMX_CON - Station: AEROPUERTO ALFONSO LOPEZ - [28025502] (11456 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.43616667,-73.24766667) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.43616667&lon=-73.24766667)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion                        |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:--------------------------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1983-04-02 00:00:00 |         28025502 | AEROPUERTO ALFONSO LOPEZ - [28025502] |   10.4362 |   -73.2477 |       138 | Sinóptica Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 2016-01-07 00:00:00 | NaT               | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    39.2 |      50 |           nan |              1200 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |       Valor |
|:------|------------:|
| count | 11456       |
| mean  |    34.6493  |
| std   |     2.18198 |
| min   |    24.8     |
| 25%   |    33.2     |
| 50%   |    34.7     |
| 75%   |    36.2     |
| max   |    41.8     |

</div>


![R.LTWB](Graph/Plot_TMX_CON_28025502_TimeSerie.png)
![R.LTWB](Graph/Plot_TMX_CON_28025502_Boxplot.png)
![R.LTWB](Graph/Plot_TMX_CON_28025502_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_28025502_DensityKDE.png)

<div align="center">



**TMX_CON - Station: CALLAO EL [28035020] (12136 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.36305556,-73.31944444) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.36305556&lon=-73.31944444)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28035020 | CALLAO EL [28035020] |   10.3631 |   -73.3194 |       110 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1968-03-15 00:00:00 | NaT               | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    34.6 |      50 |           nan |              1200 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |       Valor |
|:------|------------:|
| count | 12136       |
| mean  |    34.7338  |
| std   |     2.21035 |
| min   |    25.4     |
| 25%   |    33.2     |
| 50%   |    34.8     |
| 75%   |    36.4     |
| max   |    41.8     |

</div>


![R.LTWB](Graph/Plot_TMX_CON_28035020_TimeSerie.png)
![R.LTWB](Graph/Plot_TMX_CON_28035020_Boxplot.png)
![R.LTWB](Graph/Plot_TMX_CON_28035020_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_28035020_DensityKDE.png)

<div align="center">



**TMX_CON - Station: CICOLAC [28015030] (1127 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.48333333,-73.26666667) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.48333333&lon=-73.26666667)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion     |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-03 00:00:00 |         28015030 | CICOLAC [28015030] |   10.4833 |   -73.2667 |       180 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1964-01-15 00:00:00 | 1988-05-15 00:00:00 | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    34.3 |      50 |           nan |              1200 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |      Valor |
|:------|-----------:|
| count | 1127       |
| mean  |   34.5657  |
| std   |    1.85704 |
| min   |   26.3     |
| 25%   |   33.4     |
| 50%   |   34.6     |
| 75%   |   35.8     |
| max   |   40.4     |

</div>


![R.LTWB](Graph/Plot_TMX_CON_28015030_TimeSerie.png)
![R.LTWB](Graph/Plot_TMX_CON_28015030_Boxplot.png)
![R.LTWB](Graph/Plot_TMX_CON_28015030_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_28015030_DensityKDE.png)

<div align="center">



**TMX_CON - Station: GUATAPURI - AUT [28035070] (42 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.73213889,-73.39241667) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.73213889&lon=-73.39241667)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion             |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 2012-12-01 00:00:00 |         28035070 | GUATAPURI - AUT [28035070] |   10.7321 |   -73.3924 |      1315 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 2006-02-26 00:00:00 | 2018-06-11 10:25:00 | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    35.8 |      50 |           nan |              1200 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 42       |
| mean  | 37.1095  |
| std   |  1.26738 |
| min   | 34       |
| 25%   | 36.6     |
| 50%   | 37.4     |
| 75%   | 38       |
| max   | 39.2     |

</div>


![R.LTWB](Graph/Plot_TMX_CON_28035070_TimeSerie.png)
![R.LTWB](Graph/Plot_TMX_CON_28035070_Boxplot.png)
![R.LTWB](Graph/Plot_TMX_CON_28035070_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_28035070_DensityKDE.png)

<div align="center">



**TMX_CON - Station: RINCON EL [28025020] (12966 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.27138889,-73.13138889) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.27138889&lon=-73.13138889)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-02-01 00:00:00 |         28025020 | RINCON EL [28025020] |   10.2714 |   -73.1314 |       350 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | San Diego   | 1964-02-15 00:00:00 | NaT               | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    32.3 |      50 |           nan |              1200 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |       Valor |
|:------|------------:|
| count | 12966       |
| mean  |    32.6602  |
| std   |     2.08594 |
| min   |    24.6     |
| 25%   |    31.3     |
| 50%   |    32.7     |
| 75%   |    34.2     |
| max   |    39.7     |

</div>


![R.LTWB](Graph/Plot_TMX_CON_28025020_TimeSerie.png)
![R.LTWB](Graph/Plot_TMX_CON_28025020_Boxplot.png)
![R.LTWB](Graph/Plot_TMX_CON_28025020_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_28025020_DensityKDE.png)

<div align="center">



**TMX_CON - Station: SAN JOSE D ORIENTE [28025040] (2613 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.35,-73.05) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.35&lon=-73.05)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion                |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-02 00:00:00 |         28025040 | SAN JOSE D ORIENTE [28025040] |     10.35 |     -73.05 |       850 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | La Paz      | 1975-08-15 00:00:00 | 1998-05-15 00:00:00 | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    29.8 |      50 |           nan |              1200 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |      Valor |
|:------|-----------:|
| count | 2613       |
| mean  |   29.7907  |
| std   |    1.74453 |
| min   |   22.4     |
| 25%   |   28.6     |
| 50%   |   30       |
| 75%   |   31       |
| max   |   39.2     |

</div>


![R.LTWB](Graph/Plot_TMX_CON_28025040_TimeSerie.png)
![R.LTWB](Graph/Plot_TMX_CON_28025040_Boxplot.png)
![R.LTWB](Graph/Plot_TMX_CON_28025040_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_28025040_DensityKDE.png)

<div align="center">



**TMX_CON - Station: LA PAULINA - AUT [15065040] (3465 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.89813889,-72.82847222) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.89813889&lon=-72.82847222)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion              |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-04-01 00:00:00 |         15065040 | LA PAULINA - AUT [15065040] |   10.8981 |   -72.8285 |       170 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | Fonseca     | 1966-09-15 00:00:00 | NaT               | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    35.2 |      50 |           nan |              1200 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |      Valor |
|:------|-----------:|
| count | 3465       |
| mean  |   34.0803  |
| std   |    1.83791 |
| min   |   25.1     |
| 25%   |   33       |
| 50%   |   34.2     |
| 75%   |   35.4     |
| max   |   39.4     |

</div>


![R.LTWB](Graph/Plot_TMX_CON_15065040_TimeSerie.png)
![R.LTWB](Graph/Plot_TMX_CON_15065040_Boxplot.png)
![R.LTWB](Graph/Plot_TMX_CON_15065040_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_15065040_DensityKDE.png)

<div align="center">



**TMX_CON - Station: URUMITA [28015070] (12645 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.56638889,-73.01638889) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.56638889&lon=-73.01638889)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion     |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28015070 | URUMITA [28015070] |   10.5664 |   -73.0164 |       255 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | Urumita     | 1975-08-15 00:00:00 | NaT               | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    32.4 |      50 |           nan |              1200 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |       Valor |
|:------|------------:|
| count | 12645       |
| mean  |    33.7017  |
| std   |     2.18347 |
| min   |    23.8     |
| 25%   |    32.2     |
| 50%   |    33.6     |
| 75%   |    35.2     |
| max   |    42.2     |

</div>


![R.LTWB](Graph/Plot_TMX_CON_28015070_TimeSerie.png)
![R.LTWB](Graph/Plot_TMX_CON_28015070_Boxplot.png)
![R.LTWB](Graph/Plot_TMX_CON_28015070_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_28015070_DensityKDE.png)

<div align="center">



**TMX_CON - Station: AEROPUERTO LAS FLORES [25025090] (8486 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.046333333,-73.97083333) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.046333333&lon=-73.97083333)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion                   |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25025090 | AEROPUERTO LAS FLORES [25025090] |   9.04633 |   -73.9708 |        34 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | El Banco    | 1952-02-15 00:00:00 | NaT               | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    33.6 |      50 |           nan |              1200 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |     Valor |
|:------|----------:|
| count | 8486      |
| mean  |   33.5555 |
| std   |    1.8415 |
| min   |   26.4    |
| 25%   |   32.4    |
| 50%   |   33.6    |
| 75%   |   34.8    |
| max   |   40      |

</div>


![R.LTWB](Graph/Plot_TMX_CON_25025090_TimeSerie.png)
![R.LTWB](Graph/Plot_TMX_CON_25025090_Boxplot.png)
![R.LTWB](Graph/Plot_TMX_CON_25025090_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_25025090_DensityKDE.png)

<div align="center">



**TMX_CON - Station: LOS ALAMOS - AUT [25025002] (7701 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.304055556,-74.27363889) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.304055556&lon=-74.27363889)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion              |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio                   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:----------------------------|:--------------------|:------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1985-01-06 00:00:00 |         25025002 | LOS ALAMOS - AUT [25025002] |   9.30406 |   -74.2736 |        25 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | San Sebastián De Buenavista | 2013-05-05 00:00:00 | NaT               | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    32.4 |      50 |           nan |              1200 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |      Valor |
|:------|-----------:|
| count | 7701       |
| mean  |   34.3217  |
| std   |    2.06657 |
| min   |   23       |
| 25%   |   33       |
| 50%   |   34.2     |
| 75%   |   35.6     |
| max   |   44       |

</div>


![R.LTWB](Graph/Plot_TMX_CON_25025002_TimeSerie.png)
![R.LTWB](Graph/Plot_TMX_CON_25025002_Boxplot.png)
![R.LTWB](Graph/Plot_TMX_CON_25025002_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_25025002_DensityKDE.png)

<div align="center">



**TMX_CON - Station: PADELMA [29065020] (9406 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.72111111,-74.19972222) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.72111111&lon=-74.19972222)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion     |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio     | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:--------------|:--------------------|:------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-03-01 00:00:00 |         29065020 | PADELMA [29065020] |   10.7211 |   -74.1997 |        20 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1967-08-15 00:00:00 | NaT               | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    33.2 |      50 |           nan |              1200 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |      Valor |
|:------|-----------:|
| count | 9406       |
| mean  |   34.1372  |
| std   |    1.63127 |
| min   |   26       |
| 25%   |   33       |
| 50%   |   34.2     |
| 75%   |   35.2     |
| max   |   39.8     |

</div>


![R.LTWB](Graph/Plot_TMX_CON_29065020_TimeSerie.png)
![R.LTWB](Graph/Plot_TMX_CON_29065020_Boxplot.png)
![R.LTWB](Graph/Plot_TMX_CON_29065020_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_29065020_DensityKDE.png)

<div align="center">



**TMX_CON - Station: PRADO SEVILLA [29065030] (10537 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.76416667,-74.15472222) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.76416667&lon=-74.15472222)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion           |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio     | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:--------------|:--------------------|:--------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29065030 | PRADO SEVILLA [29065030] |   10.7642 |   -74.1547 |        18 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1970-07-15 00:00:00 | 2019-02-07 11:32:00 | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    33.2 |      50 |           nan |              1200 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |      Valor |
|:------|-----------:|
| count | 10537      |
| mean  |    33.3129 |
| std   |     1.4911 |
| min   |    24.8    |
| 25%   |    32.4    |
| 50%   |    33.4    |
| 75%   |    34.2    |
| max   |    38.6    |

</div>


![R.LTWB](Graph/Plot_TMX_CON_29065030_TimeSerie.png)
![R.LTWB](Graph/Plot_TMX_CON_29065030_Boxplot.png)
![R.LTWB](Graph/Plot_TMX_CON_29065030_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_29065030_DensityKDE.png)

<div align="center">



**TMX_CON - Station: SEIS EL [25025300] (10066 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.683666667,-74.32227778) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.683666667&lon=-74.32227778)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion     |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio                   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:----------------------------|:--------------------|:------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1985-05-01 00:00:00 |         25025300 | SEIS EL [25025300] |   9.68367 |   -74.3223 |        50 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | San Sebastián De Buenavista | 1984-11-15 00:00:00 | NaT               | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    35.2 |      50 |           nan |              1200 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |      Valor |
|:------|-----------:|
| count | 10066      |
| mean  |    34.5617 |
| std   |     2.3698 |
| min   |    25.2    |
| 25%   |    32.8    |
| 50%   |    34.6    |
| 75%   |    36.2    |
| max   |    41.8    |

</div>


![R.LTWB](Graph/Plot_TMX_CON_25025300_TimeSerie.png)
![R.LTWB](Graph/Plot_TMX_CON_25025300_Boxplot.png)
![R.LTWB](Graph/Plot_TMX_CON_25025300_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_25025300_DensityKDE.png)

<div align="center">



**TMX_CON - Station: YE LA [15015020] (8859 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.99241667,-74.21113889) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.99241667&lon=-74.21113889)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion   |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-----------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         15015020 | YE LA [15015020] |   10.9924 |   -74.2111 |        20 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Ciénaga     | 1967-07-15 00:00:00 | 2019-02-07 11:34:00 | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    32.2 |      50 |           nan |              1200 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |      Valor |
|:------|-----------:|
| count | 8859       |
| mean  |   33.0729  |
| std   |    1.48932 |
| min   |   25.4     |
| 25%   |   32.2     |
| 50%   |   33.2     |
| 75%   |   34.2     |
| max   |   38.4     |

</div>


![R.LTWB](Graph/Plot_TMX_CON_15015020_TimeSerie.png)
![R.LTWB](Graph/Plot_TMX_CON_15015020_Boxplot.png)
![R.LTWB](Graph/Plot_TMX_CON_15015020_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_15015020_DensityKDE.png)

<div align="center">



**TMX_CON - Station: ZACAPA [29065010] (893 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.58333333,-74.25) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.58333333&lon=-74.25)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion    |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1981-01-01 00:00:00 |         29065010 | ZACAPA [29065010] |   10.5833 |     -74.25 |        30 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | El Retén    | 1967-07-15 00:00:00 | 1990-04-15 00:00:00 | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    33.6 |      50 |           nan |              1200 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |     Valor |
|:------|----------:|
| count | 893       |
| mean  |  33.5259  |
| std   |   1.58034 |
| min   |  29.4     |
| 25%   |  32.4     |
| 50%   |  33.6     |
| 75%   |  34.6     |
| max   |  37.2     |

</div>


![R.LTWB](Graph/Plot_TMX_CON_29065010_TimeSerie.png)
![R.LTWB](Graph/Plot_TMX_CON_29065010_Boxplot.png)
![R.LTWB](Graph/Plot_TMX_CON_29065010_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_29065010_DensityKDE.png)


### Analysis from 1980 to 2021 for Etiqueta == "TMN_CON": 209823 (40.75%)

Pivot table: [Pivot_TMN_CON.csv](Pivot_TMN_CON.csv)
![R.LTWB](Graph/Plot_TMN_CON_TimeSerie.png)
![R.LTWB](Graph/Plot_TMN_CON_DensityKDE.png)

<div align="center">



**TMN_CON - Station: AEROPUERTO ALFONSO LOPEZ - [28025502] (12238 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.43616667,-73.24766667) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.43616667&lon=-73.24766667)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion                        |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:--------------------------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-02 00:00:00 |         28025502 | AEROPUERTO ALFONSO LOPEZ - [28025502] |   10.4362 |   -73.2477 |       138 | Sinóptica Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 2016-01-07 00:00:00 | NaT               | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |      24 |      50 |           nan |              1200 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |       Valor |
|:------|------------:|
| count | 12238       |
| mean  |    23.8861  |
| std   |     1.27915 |
| min   |    18.4     |
| 25%   |    23       |
| 50%   |    23.8     |
| 75%   |    24.8     |
| max   |    28.6     |

</div>


![R.LTWB](Graph/Plot_TMN_CON_28025502_TimeSerie.png)
![R.LTWB](Graph/Plot_TMN_CON_28025502_Boxplot.png)
![R.LTWB](Graph/Plot_TMN_CON_28025502_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_28025502_DensityKDE.png)

<div align="center">



**TMN_CON - Station: CENTENARIO HACIENDA [28025090] (11867 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.85025,-73.26547222) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.85025&lon=-73.26547222)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion                 |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio       | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:----------------|:--------------------|:------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1981-01-03 00:00:00 |         28025090 | CENTENARIO HACIENDA [28025090] |   9.85025 |   -73.2655 |       100 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Agustín Codazzi | 1976-12-15 00:00:00 | NaT               | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    22.2 |      50 |           nan |              1200 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |       Valor |
|:------|------------:|
| count | 11867       |
| mean  |    22.4272  |
| std   |     1.67337 |
| min   |    15       |
| 25%   |    21.6     |
| 50%   |    22.8     |
| 75%   |    23.6     |
| max   |    27.4     |

</div>


![R.LTWB](Graph/Plot_TMN_CON_28025090_TimeSerie.png)
![R.LTWB](Graph/Plot_TMN_CON_28025090_Boxplot.png)
![R.LTWB](Graph/Plot_TMN_CON_28025090_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_28025090_DensityKDE.png)

<div align="center">



**TMN_CON - Station: CHIRIGUANA [25025250] (12340 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.361027778,-73.59338889) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.361027778&lon=-73.59338889)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion        |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1981-04-01 00:00:00 |         25025250 | CHIRIGUANA [25025250] |   9.36103 |   -73.5934 |        40 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Chiriguaná  | 1973-06-15 00:00:00 | NaT               | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    22.2 |      50 |           nan |              1200 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |       Valor |
|:------|------------:|
| count | 12340       |
| mean  |    22.3963  |
| std   |     1.63717 |
| min   |    17       |
| 25%   |    21.2     |
| 50%   |    22.4     |
| 75%   |    23.8     |
| max   |    27.1     |

</div>


![R.LTWB](Graph/Plot_TMN_CON_25025250_TimeSerie.png)
![R.LTWB](Graph/Plot_TMN_CON_25025250_Boxplot.png)
![R.LTWB](Graph/Plot_TMN_CON_25025250_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_25025250_DensityKDE.png)

<div align="center">



**TMN_CON - Station: CICOLAC [28015030] (1404 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.48333333,-73.26666667) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.48333333&lon=-73.26666667)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion     |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-02 00:00:00 |         28015030 | CICOLAC [28015030] |   10.4833 |   -73.2667 |       180 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1964-01-15 00:00:00 | 1988-05-15 00:00:00 | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    23.3 |      50 |           nan |              1200 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |      Valor |
|:------|-----------:|
| count | 1404       |
| mean  |   22.9291  |
| std   |    1.32774 |
| min   |   10       |
| 25%   |   22.2     |
| 50%   |   23       |
| 75%   |   23.8     |
| max   |   26.8     |

</div>


![R.LTWB](Graph/Plot_TMN_CON_28015030_TimeSerie.png)
![R.LTWB](Graph/Plot_TMN_CON_28015030_Boxplot.png)
![R.LTWB](Graph/Plot_TMN_CON_28015030_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_28015030_DensityKDE.png)

<div align="center">



**TMN_CON - Station: COLEGIO AGROPECUARIO PAILITAS  - AUT [25025330] (9275 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=8.954222222,-73.63008333) or [Openstreet Map](https://www.openstreetmap.org/query?lat=8.954222222&lon=-73.63008333)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion                                  |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------------------------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1987-09-14 00:00:00 |         25025330 | COLEGIO AGROPECUARIO PAILITAS  - AUT [25025330] |   8.95422 |   -73.6301 |        50 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Pailitas    | 1987-09-15 00:00:00 | NaT               | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |      23 |      50 |           nan |              1200 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |     Valor |
|:------|----------:|
| count | 9275      |
| mean  |   22.7791 |
| std   |    1.6933 |
| min   |   13.1    |
| 25%   |   21.8    |
| 50%   |   23      |
| 75%   |   24      |
| max   |   28.6    |

</div>


![R.LTWB](Graph/Plot_TMN_CON_25025330_TimeSerie.png)
![R.LTWB](Graph/Plot_TMN_CON_25025330_Boxplot.png)
![R.LTWB](Graph/Plot_TMN_CON_25025330_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_25025330_DensityKDE.png)

<div align="center">



**TMN_CON - Station: LA GLORIA [23215060] (1248 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=8.615277778,-73.800555556) or [Openstreet Map](https://www.openstreetmap.org/query?lat=8.615277778&lon=-73.800555556)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                          | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:---------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1983-10-27 00:00:00 |         23215060 | LA GLORIA [23215060] |   8.61528 |   -73.8006 |        35 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 08 - Santanderes-Arauca | Cesar          | La Gloria   | 1995-05-15 00:00:00 | 2018-06-19 10:35:00 | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    20.2 |      50 |           nan |              1200 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |      Valor |
|:------|-----------:|
| count | 1248       |
| mean  |   23.6837  |
| std   |    1.20744 |
| min   |   16.6     |
| 25%   |   23       |
| 50%   |   23.8     |
| 75%   |   24.6     |
| max   |   26.8     |

</div>


![R.LTWB](Graph/Plot_TMN_CON_23215060_TimeSerie.png)
![R.LTWB](Graph/Plot_TMN_CON_23215060_Boxplot.png)
![R.LTWB](Graph/Plot_TMN_CON_23215060_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_23215060_DensityKDE.png)

<div align="center">



**TMN_CON - Station: MOTILONIA CODAZZI [28025070] (13818 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.00180556,-73.24938889) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.00180556&lon=-73.24938889)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion               |   Latitud |   Longitud |   Altitud | Categoria         | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio       | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-----------------------------|----------:|-----------:|----------:|:------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:----------------|:--------------------|:------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28025070 | MOTILONIA CODAZZI [28025070] |   10.0018 |   -73.2494 |       180 | Agrometeorológica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Agustín Codazzi | 1956-01-15 00:00:00 | NaT               | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    22.8 |      50 |           nan |              1200 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |       Valor |
|:------|------------:|
| count | 13818       |
| mean  |    23.7666  |
| std   |     1.54724 |
| min   |    17.4     |
| 25%   |    22.8     |
| 50%   |    23.8     |
| 75%   |    25       |
| max   |    28.6     |

</div>


![R.LTWB](Graph/Plot_TMN_CON_28025070_TimeSerie.png)
![R.LTWB](Graph/Plot_TMN_CON_28025070_Boxplot.png)
![R.LTWB](Graph/Plot_TMN_CON_28025070_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_28025070_DensityKDE.png)

<div align="center">



**TMN_CON - Station: RINCON EL [28025020] (13452 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.27138889,-73.13138889) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.27138889&lon=-73.13138889)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-02-02 00:00:00 |         28025020 | RINCON EL [28025020] |   10.2714 |   -73.1314 |       350 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | San Diego   | 1964-02-15 00:00:00 | NaT               | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    18.8 |      50 |           nan |              1200 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |       Valor |
|:------|------------:|
| count | 13452       |
| mean  |    20.547   |
| std   |     1.73534 |
| min   |    12       |
| 25%   |    19.6     |
| 50%   |    20.8     |
| 75%   |    21.8     |
| max   |    26       |

</div>


![R.LTWB](Graph/Plot_TMN_CON_28025020_TimeSerie.png)
![R.LTWB](Graph/Plot_TMN_CON_28025020_Boxplot.png)
![R.LTWB](Graph/Plot_TMN_CON_28025020_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_28025020_DensityKDE.png)

<div align="center">



**TMN_CON - Station: SAN JOSE D ORIENTE [28025040] (3231 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.35,-73.05) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.35&lon=-73.05)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion                |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28025040 | SAN JOSE D ORIENTE [28025040] |     10.35 |     -73.05 |       850 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | La Paz      | 1975-08-15 00:00:00 | 1998-05-15 00:00:00 | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    20.2 |      50 |           nan |              1200 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |      Valor |
|:------|-----------:|
| count | 3231       |
| mean  |   18.674   |
| std   |    2.11514 |
| min   |    8.4     |
| 25%   |   18       |
| 50%   |   19.2     |
| 75%   |   20       |
| max   |   27.4     |

</div>


![R.LTWB](Graph/Plot_TMN_CON_28025040_TimeSerie.png)
![R.LTWB](Graph/Plot_TMN_CON_28025040_Boxplot.png)
![R.LTWB](Graph/Plot_TMN_CON_28025040_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_28025040_DensityKDE.png)

<div align="center">



**TMN_CON - Station: SOCOMBA [28025080] (7636 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.686666667,-73.24055556) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.686666667&lon=-73.24055556)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion     |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28025080 | SOCOMBA [28025080] |   9.68667 |   -73.2406 |       170 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Becerrill   | 1976-12-15 00:00:00 | 2019-02-07 11:41:00 | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    21.8 |      50 |           nan |              1200 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |      Valor |
|:------|-----------:|
| count | 7636       |
| mean  |   21.7751  |
| std   |    1.87894 |
| min   |   15.2     |
| 25%   |   20.4     |
| 50%   |   22.2     |
| 75%   |   23.2     |
| max   |   27       |

</div>


![R.LTWB](Graph/Plot_TMN_CON_28025080_TimeSerie.png)
![R.LTWB](Graph/Plot_TMN_CON_28025080_Boxplot.png)
![R.LTWB](Graph/Plot_TMN_CON_28025080_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_28025080_DensityKDE.png)

<div align="center">



**TMN_CON - Station: ALGARROBO [28045020] (1052 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.15,-74.06666667) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.15&lon=-74.06666667)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1983-01-02 00:00:00 |         28045020 | ALGARROBO [28045020] |     10.15 |   -74.0667 |        60 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | El Copey    | 1964-02-15 00:00:00 | 1987-04-15 00:00:00 | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    17.6 |      50 |           nan |              1200 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |      Valor |
|:------|-----------:|
| count | 1052       |
| mean  |   21.2974  |
| std   |    1.79272 |
| min   |   14.6     |
| 25%   |   20.2     |
| 50%   |   21.6     |
| 75%   |   22.6     |
| max   |   26.4     |

</div>


![R.LTWB](Graph/Plot_TMN_CON_28045020_TimeSerie.png)
![R.LTWB](Graph/Plot_TMN_CON_28045020_Boxplot.png)
![R.LTWB](Graph/Plot_TMN_CON_28045020_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_28045020_DensityKDE.png)

<div align="center">



**TMN_CON - Station: CALLAO EL [28035020] (11824 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.36305556,-73.31944444) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.36305556&lon=-73.31944444)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28035020 | CALLAO EL [28035020] |   10.3631 |   -73.3194 |       110 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1968-03-15 00:00:00 | NaT               | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    19.4 |      50 |           nan |              1200 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |       Valor |
|:------|------------:|
| count | 11824       |
| mean  |    22.8005  |
| std   |     1.82844 |
| min   |    15.8     |
| 25%   |    21.8     |
| 50%   |    23       |
| 75%   |    24       |
| max   |    28.6     |

</div>


![R.LTWB](Graph/Plot_TMN_CON_28035020_TimeSerie.png)
![R.LTWB](Graph/Plot_TMN_CON_28035020_Boxplot.png)
![R.LTWB](Graph/Plot_TMN_CON_28035020_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_28035020_DensityKDE.png)

<div align="center">



**TMN_CON - Station: GUAIRA LA HACIENDA [28045040] (1274 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.616666667,-73.8) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.616666667&lon=-73.8)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion                |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1987-09-11 00:00:00 |         28045040 | GUAIRA LA HACIENDA [28045040] |   9.61667 |      -73.8 |        50 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | El Paso     | 1987-09-15 00:00:00 | 1994-07-15 00:00:00 | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |      23 |      50 |           nan |              1200 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |      Valor |
|:------|-----------:|
| count | 1274       |
| mean  |   23.128   |
| std   |    1.26701 |
| min   |   14.6     |
| 25%   |   22.4     |
| 50%   |   23.2     |
| 75%   |   24       |
| max   |   26.6     |

</div>


![R.LTWB](Graph/Plot_TMN_CON_28045040_TimeSerie.png)
![R.LTWB](Graph/Plot_TMN_CON_28045040_Boxplot.png)
![R.LTWB](Graph/Plot_TMN_CON_28045040_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_28045040_DensityKDE.png)

<div align="center">



**TMN_CON - Station: GUATAPURI - AUT [28035070] (42 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.73213889,-73.39241667) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.73213889&lon=-73.39241667)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion             |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 2012-12-01 00:00:00 |         28035070 | GUATAPURI - AUT [28035070] |   10.7321 |   -73.3924 |      1315 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 2006-02-26 00:00:00 | 2018-06-11 10:25:00 | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    21.8 |      50 |           nan |              1200 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 42       |
| mean  | 22.0286  |
| std   |  1.01844 |
| min   | 20.6     |
| 25%   | 21.4     |
| 50%   | 21.8     |
| 75%   | 22.6     |
| max   | 25.6     |

</div>


![R.LTWB](Graph/Plot_TMN_CON_28035070_TimeSerie.png)
![R.LTWB](Graph/Plot_TMN_CON_28035070_Boxplot.png)
![R.LTWB](Graph/Plot_TMN_CON_28035070_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_28035070_DensityKDE.png)

<div align="center">



**TMN_CON - Station: GUAYMARAL [28035040] (13405 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.904916667,-73.64752778) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.904916667&lon=-73.64752778)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1981-06-01 00:00:00 |         28035040 | GUAYMARAL [28035040] |   9.90492 |   -73.6475 |        50 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1972-08-15 00:00:00 | NaT               | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    24.2 |      50 |           nan |              1200 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |       Valor |
|:------|------------:|
| count | 13405       |
| mean  |    24.269   |
| std   |     1.23846 |
| min   |    17.2     |
| 25%   |    23.4     |
| 50%   |    24.2     |
| 75%   |    25       |
| max   |    28.6     |

</div>


![R.LTWB](Graph/Plot_TMN_CON_28035040_TimeSerie.png)
![R.LTWB](Graph/Plot_TMN_CON_28035040_Boxplot.png)
![R.LTWB](Graph/Plot_TMN_CON_28035040_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_28035040_DensityKDE.png)

<div align="center">



**TMN_CON - Station: VILLA ROSA [28035010] (10557 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.19066667,-73.54738889) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.19066667&lon=-73.54738889)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion        |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-03 00:00:00 |         28035010 | VILLA ROSA [28035010] |   10.1907 |   -73.5474 |        70 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1968-03-15 00:00:00 | NaT               | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    22.4 |      50 |           nan |              1200 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |       Valor |
|:------|------------:|
| count | 10557       |
| mean  |    23.3278  |
| std   |     1.49337 |
| min   |    13.4     |
| 25%   |    22.6     |
| 50%   |    23.4     |
| 75%   |    24.2     |
| max   |    28.8     |

</div>


![R.LTWB](Graph/Plot_TMN_CON_28035010_TimeSerie.png)
![R.LTWB](Graph/Plot_TMN_CON_28035010_Boxplot.png)
![R.LTWB](Graph/Plot_TMN_CON_28035010_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_28035010_DensityKDE.png)

<div align="center">



**TMN_CON - Station: LA PAULINA - AUT [15065040] (4949 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.89813889,-72.82847222) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.89813889&lon=-72.82847222)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion              |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-09-05 00:00:00 |         15065040 | LA PAULINA - AUT [15065040] |   10.8981 |   -72.8285 |       170 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | Fonseca     | 1966-09-15 00:00:00 | NaT               | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |      22 |      50 |           nan |              1200 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |      Valor |
|:------|-----------:|
| count | 4949       |
| mean  |   22.9664  |
| std   |    1.75384 |
| min   |   12.4     |
| 25%   |   22.2     |
| 50%   |   23.2     |
| 75%   |   24.2     |
| max   |   27.8     |

</div>


![R.LTWB](Graph/Plot_TMN_CON_15065040_TimeSerie.png)
![R.LTWB](Graph/Plot_TMN_CON_15065040_Boxplot.png)
![R.LTWB](Graph/Plot_TMN_CON_15065040_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_15065040_DensityKDE.png)

<div align="center">



**TMN_CON - Station: URUMITA [28015070] (12475 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.56638889,-73.01638889) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.56638889&lon=-73.01638889)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion     |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28015070 | URUMITA [28015070] |   10.5664 |   -73.0164 |       255 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | Urumita     | 1975-08-15 00:00:00 | NaT               | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |      23 |      50 |           nan |              1200 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |       Valor |
|:------|------------:|
| count | 12475       |
| mean  |    22.34    |
| std   |     1.33165 |
| min   |    15.4     |
| 25%   |    21.5     |
| 50%   |    22.5     |
| 75%   |    23.2     |
| max   |    26.2     |

</div>


![R.LTWB](Graph/Plot_TMN_CON_28015070_TimeSerie.png)
![R.LTWB](Graph/Plot_TMN_CON_28015070_Boxplot.png)
![R.LTWB](Graph/Plot_TMN_CON_28015070_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_28015070_DensityKDE.png)

<div align="center">



**TMN_CON - Station: LOS ALAMOS - AUT [25025002] (10733 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.304055556,-74.27363889) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.304055556&lon=-74.27363889)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion              |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio                   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:----------------------------|:--------------------|:------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1985-01-06 00:00:00 |         25025002 | LOS ALAMOS - AUT [25025002] |   9.30406 |   -74.2736 |        25 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | San Sebastián De Buenavista | 2013-05-05 00:00:00 | NaT               | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    23.4 |      50 |           nan |              1200 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |       Valor |
|:------|------------:|
| count | 10733       |
| mean  |    22.9428  |
| std   |     1.56303 |
| min   |    16.8     |
| 25%   |    22       |
| 50%   |    23       |
| 75%   |    24       |
| max   |    27.2     |

</div>


![R.LTWB](Graph/Plot_TMN_CON_25025002_TimeSerie.png)
![R.LTWB](Graph/Plot_TMN_CON_25025002_Boxplot.png)
![R.LTWB](Graph/Plot_TMN_CON_25025002_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_25025002_DensityKDE.png)

<div align="center">



**TMN_CON - Station: YE LA [15015020] (9964 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.99241667,-74.21113889) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.99241667&lon=-74.21113889)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion   |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-----------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         15015020 | YE LA [15015020] |   10.9924 |   -74.2111 |        20 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Ciénaga     | 1967-07-15 00:00:00 | 2019-02-07 11:34:00 | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    23.2 |      50 |           nan |              1200 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |      Valor |
|:------|-----------:|
| count | 9964       |
| mean  |   22.1888  |
| std   |    1.60856 |
| min   |   16       |
| 25%   |   21.2     |
| 50%   |   22.4     |
| 75%   |   23.2     |
| max   |   26.8     |

</div>


![R.LTWB](Graph/Plot_TMN_CON_15015020_TimeSerie.png)
![R.LTWB](Graph/Plot_TMN_CON_15015020_Boxplot.png)
![R.LTWB](Graph/Plot_TMN_CON_15015020_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_15015020_DensityKDE.png)

<div align="center">



**TMN_CON - Station: AEROPUERTO LAS FLORES [25025090] (9774 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.046333333,-73.97083333) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.046333333&lon=-73.97083333)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion                   |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25025090 | AEROPUERTO LAS FLORES [25025090] |   9.04633 |   -73.9708 |        34 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | El Banco    | 1952-02-15 00:00:00 | NaT               | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    24.2 |      50 |           nan |              1200 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |      Valor |
|:------|-----------:|
| count | 9774       |
| mean  |   23.5651  |
| std   |    1.53376 |
| min   |   17       |
| 25%   |   22.6     |
| 50%   |   23.6     |
| 75%   |   24.8     |
| max   |   28       |

</div>


![R.LTWB](Graph/Plot_TMN_CON_25025090_TimeSerie.png)
![R.LTWB](Graph/Plot_TMN_CON_25025090_Boxplot.png)
![R.LTWB](Graph/Plot_TMN_CON_25025090_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_25025090_DensityKDE.png)

<div align="center">



**TMN_CON - Station: PADELMA [29065020] (12983 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.72111111,-74.19972222) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.72111111&lon=-74.19972222)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion     |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio     | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:--------------|:--------------------|:------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-03-01 00:00:00 |         29065020 | PADELMA [29065020] |   10.7211 |   -74.1997 |        20 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1967-08-15 00:00:00 | NaT               | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    21.8 |      50 |           nan |              1200 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |       Valor |
|:------|------------:|
| count | 12983       |
| mean  |    22.327   |
| std   |     1.85521 |
| min   |    14.2     |
| 25%   |    21.2     |
| 50%   |    22.6     |
| 75%   |    23.6     |
| max   |    27.4     |

</div>


![R.LTWB](Graph/Plot_TMN_CON_29065020_TimeSerie.png)
![R.LTWB](Graph/Plot_TMN_CON_29065020_Boxplot.png)
![R.LTWB](Graph/Plot_TMN_CON_29065020_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_29065020_DensityKDE.png)

<div align="center">



**TMN_CON - Station: PRADO SEVILLA [29065030] (11526 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.76416667,-74.15472222) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.76416667&lon=-74.15472222)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion           |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio     | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:--------------|:--------------------|:--------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29065030 | PRADO SEVILLA [29065030] |   10.7642 |   -74.1547 |        18 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1970-07-15 00:00:00 | 2019-02-07 11:32:00 | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    21.4 |      50 |           nan |              1200 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |       Valor |
|:------|------------:|
| count | 11526       |
| mean  |    21.8104  |
| std   |     1.55983 |
| min   |    14       |
| 25%   |    20.8     |
| 50%   |    22       |
| 75%   |    23       |
| max   |    27       |

</div>


![R.LTWB](Graph/Plot_TMN_CON_29065030_TimeSerie.png)
![R.LTWB](Graph/Plot_TMN_CON_29065030_Boxplot.png)
![R.LTWB](Graph/Plot_TMN_CON_29065030_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_29065030_DensityKDE.png)

<div align="center">



**TMN_CON - Station: SEIS EL [25025300] (11693 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.683666667,-74.32227778) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.683666667&lon=-74.32227778)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion     |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio                   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:----------------------------|:--------------------|:------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1985-05-01 00:00:00 |         25025300 | SEIS EL [25025300] |   9.68367 |   -74.3223 |        50 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | San Sebastián De Buenavista | 1984-11-15 00:00:00 | NaT               | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    20.4 |      50 |           nan |              1200 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |       Valor |
|:------|------------:|
| count | 11693       |
| mean  |    22.9902  |
| std   |     1.75271 |
| min   |    15.4     |
| 25%   |    22       |
| 50%   |    23.2     |
| 75%   |    24.2     |
| max   |    27.8     |

</div>


![R.LTWB](Graph/Plot_TMN_CON_25025300_TimeSerie.png)
![R.LTWB](Graph/Plot_TMN_CON_25025300_Boxplot.png)
![R.LTWB](Graph/Plot_TMN_CON_25025300_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_25025300_DensityKDE.png)

<div align="center">



**TMN_CON - Station: ZACAPA [29065010] (1063 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.58333333,-74.25) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.58333333&lon=-74.25)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion    |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29065010 | ZACAPA [29065010] |   10.5833 |     -74.25 |        30 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | El Retén    | 1967-07-15 00:00:00 | 1990-04-15 00:00:00 | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    21.4 |      50 |           nan |              1200 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |      Valor |
|:------|-----------:|
| count | 1063       |
| mean  |   21.3162  |
| std   |    1.60256 |
| min   |   15.2     |
| 25%   |   20.4     |
| 50%   |   21.4     |
| 75%   |   22.4     |
| max   |   25.2     |

</div>


![R.LTWB](Graph/Plot_TMN_CON_29065010_TimeSerie.png)
![R.LTWB](Graph/Plot_TMN_CON_29065010_Boxplot.png)
![R.LTWB](Graph/Plot_TMN_CON_29065010_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_29065010_DensityKDE.png)


### Analysis from 1980 to 2021 for Etiqueta == "EV_TT_D": 4821 (0.94%)

Pivot table: [Pivot_EV_TT_D.csv](Pivot_EV_TT_D.csv)
![R.LTWB](Graph/Plot_EV_TT_D_TimeSerie.png)
![R.LTWB](Graph/Plot_EV_TT_D_DensityKDE.png)

<div align="center">



**EV_TT_D - Station: LA GRAN VIA - AUT [29065130] (4821 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.85,-74.13333333) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.85&lon=-74.13333333)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion               |   Latitud |   Longitud |   Altitud | Categoria         | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio     | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie         | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-----------------------------|----------:|-----------:|----------:|:------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:--------------|:--------------------|:------------------|:--------------|:-----------|:-------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 2008-10-20 00:00:00 |         29065130 | LA GRAN VIA - AUT [29065130] |     10.85 |   -74.1333 |        30 | Agrometeorológica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 2008-01-10 00:00:00 | NaT               | EVAPORACION   | EV_TT_D    | Evaporación total diaria | Diaria       |       0 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 4821     |
| mean  |  281.089 |
| std   |  625.398 |
| min   | -176     |
| 25%   |    0     |
| 50%   |    0     |
| 75%   |  139     |
| max   | 2529     |

</div>


![R.LTWB](Graph/Plot_EV_TT_D_29065130_TimeSerie.png)
![R.LTWB](Graph/Plot_EV_TT_D_29065130_Boxplot.png)
![R.LTWB](Graph/Plot_EV_TT_D_29065130_Histogram.png)
![R.LTWB](Graph/Plot_EV_TT_D_29065130_DensityKDE.png)


### Analysis from 1980 to 2021 for Etiqueta == "Q_MEDIA_M": 21126 (4.1%)

Pivot table: [Pivot_Q_MEDIA_M.csv](Pivot_Q_MEDIA_M.csv)
![R.LTWB](Graph/Plot_Q_MEDIA_M_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: ALTO DEL ROSARIO [25027400] (489 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=8.794444444,-74.16027778) or [Openstreet Map](https://www.openstreetmap.org/query?lat=8.794444444&lon=-74.16027778)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion              |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio         | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25027400 | ALTO DEL ROSARIO [25027400] |   8.79444 |   -74.1603 |        24 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | Altos Del Rosario | 1973-07-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   128.4 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 489      |
| mean  | 151.668  |
| std   |  70.7867 |
| min   |   4.846  |
| 25%   |  95.15   |
| 50%   | 151      |
| 75%   | 205      |
| max   | 328.7    |

</div>


![R.LTWB](Graph/Plot_Q_MEDIA_M_25027400_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027400_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027400_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027400_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: ARMENIA [25027360] (462 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=8.898333333,-74.39) or [Openstreet Map](https://www.openstreetmap.org/query?lat=8.898333333&lon=-74.39)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion     |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25027360 | ARMENIA [25027360] |   8.89833 |     -74.39 |        22 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | Pinillos    | 1973-03-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |    2350 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count |  462     |
| mean  | 2790.92  |
| std   |  695.773 |
| min   | 1099.06  |
| 25%   | 2304.75  |
| 50%   | 2800.5   |
| 75%   | 3309     |
| max   | 4208.35  |

</div>


![R.LTWB](Graph/Plot_Q_MEDIA_M_25027360_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027360_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027360_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027360_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: CHAPETONA LA [25027620] (415 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=8.8875,-73.96916667) or [Openstreet Map](https://www.openstreetmap.org/query?lat=8.8875&lon=-73.96916667)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion          |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado | Calificador    |   NivelAprobacion |
|:--------------------|-----------------:|:------------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|:---------------|------------------:|
| 1980-01-01 00:00:00 |         25027620 | CHAPETONA LA [25027620] |    8.8875 |   -73.9692 |        30 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | El Peñón    | 1974-09-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   34.14 |       4 | EST. REGRESION |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 415      |
| mean  |  49.625  |
| std   |  38.9781 |
| min   |   1.309  |
| 25%   |  18.975  |
| 50%   |  38.6171 |
| 75%   |  72.32   |
| max   | 202.2    |

</div>


![R.LTWB](Graph/Plot_Q_MEDIA_M_25027620_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027620_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027620_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027620_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: LAS AGUADAS [25027490] (504 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=8.949997222,-74.049997222) or [Openstreet Map](https://www.openstreetmap.org/query?lat=8.949997222&lon=-74.049997222)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion         |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio          | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-----------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:-------------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25027490 | LAS AGUADAS [25027490] |      8.95 |     -74.05 |        27 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | San Martín De Loba | 1973-03-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |    2761 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count |  504    |
| mean  | 3661.52 |
| std   | 1335.23 |
| min   | 1292    |
| 25%   | 2605    |
| 50%   | 3467    |
| 75%   | 4490.53 |
| max   | 7841.87 |

</div>


![R.LTWB](Graph/Plot_Q_MEDIA_M_25027490_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027490_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027490_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027490_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: PALOMAS LAS [25027390] (456 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=8.830555556,-74.17055556) or [Openstreet Map](https://www.openstreetmap.org/query?lat=8.830555556&lon=-74.17055556)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion         |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio         | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-----------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25027390 | PALOMAS LAS [25027390] |   8.83056 |   -74.1706 |        24 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | Altos Del Rosario | 1973-07-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |    2550 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count |  456    |
| mean  | 3334.22 |
| std   | 1006.61 |
| min   | 1250    |
| 25%   | 2557.75 |
| 50%   | 3251    |
| 75%   | 3985    |
| max   | 6532    |

</div>


![R.LTWB](Graph/Plot_Q_MEDIA_M_25027390_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027390_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027390_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027390_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: PENONCITO [25027330] (484 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=8.989722222,-73.94722222) or [Openstreet Map](https://www.openstreetmap.org/query?lat=8.989722222&lon=-73.94722222)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25027330 | PENONCITO [25027330] |   8.98972 |   -73.9472 |        28 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | El Peñón    | 1972-09-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |    2902 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count |  484    |
| mean  | 3977.16 |
| std   | 1256.45 |
| min   | 1171.66 |
| 25%   | 3003.75 |
| 50%   | 3845    |
| 75%   | 4853.25 |
| max   | 7464    |

</div>


![R.LTWB](Graph/Plot_Q_MEDIA_M_25027330_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027330_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027330_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027330_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: REGIDOR [25027410] (423 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=8.666333333,-73.82080556) or [Openstreet Map](https://www.openstreetmap.org/query?lat=8.666333333&lon=-73.82080556)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion     |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                          | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:---------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25027410 | REGIDOR [25027410] |   8.66633 |   -73.8208 |        35 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 08 - Santanderes-Arauca | Bolivar        | Regidor     | 1973-04-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |    2200 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count |  423    |
| mean  | 4282.86 |
| std   | 1514.27 |
| min   | 1507    |
| 25%   | 3054    |
| 50%   | 4174    |
| 75%   | 5356.16 |
| max   | 8177    |

</div>


![R.LTWB](Graph/Plot_Q_MEDIA_M_25027410_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027410_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027410_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027410_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: SAN ROQUE [25027320] (473 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.07,-74.16) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.07&lon=-74.16)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25027320 | SAN ROQUE [25027320] |      9.07 |     -74.16 |        24 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | Margarita   | 1972-09-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   219.5 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count |  473     |
| mean  |  503.54  |
| std   |  278.127 |
| min   |   35.15  |
| 25%   |  288.8   |
| 50%   |  462.8   |
| 75%   |  681.7   |
| max   | 1489     |

</div>


![R.LTWB](Graph/Plot_Q_MEDIA_M_25027320_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027320_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027320_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027320_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: VICTORIA LA [25027420] (482 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=8.965,-74.22083333) or [Openstreet Map](https://www.openstreetmap.org/query?lat=8.965&lon=-74.22083333)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion         |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-----------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25027420 | VICTORIA LA [25027420] |     8.965 |   -74.2208 |        24 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | Margarita   | 1973-07-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |     198 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 482     |
| mean  | 365.328 |
| std   | 206.827 |
| min   |   4.306 |
| 25%   | 197.85  |
| 50%   | 334.85  |
| 75%   | 521.858 |
| max   | 884.3   |

</div>


![R.LTWB](Graph/Plot_Q_MEDIA_M_25027420_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027420_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027420_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027420_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: RIO NUEVO [25027630] (461 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=8.809722222,-74.25444444) or [Openstreet Map](https://www.openstreetmap.org/query?lat=8.809722222&lon=-74.25444444)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio        | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado | Calificador    |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:-----------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|:---------------|------------------:|
| 1980-01-01 00:00:00 |         25027630 | RIO NUEVO [25027630] |   8.80972 |   -74.2544 |        23 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | Barranco De Loba | 1971-08-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |    2480 |       4 | EST. REGRESION |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count |  461     |
| mean  | 2922.8   |
| std   |  719.798 |
| min   |  894.8   |
| 25%   | 2348     |
| 50%   | 2849     |
| 75%   | 3513     |
| max   | 4625     |

</div>


![R.LTWB](Graph/Plot_Q_MEDIA_M_25027630_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027630_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027630_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027630_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: ARIGUANI HACIENDA - AUT [28017120] (230 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.57419444,-73.397) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.57419444&lon=-73.397)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion                     |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado | Calificador    |   NivelAprobacion |
|:--------------------|-----------------:|:-----------------------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|:---------------|------------------:|
| 1982-01-01 00:00:00 |         28017120 | ARIGUANI HACIENDA - AUT [28017120] |   10.5742 |    -73.397 |       550 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1980-12-15 00:00:00 | 2010-09-29 00:00:00 | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   6.809 |       4 | EST. REGRESION |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |     Valor |
|:------|----------:|
| count | 230       |
| mean  |  16.453   |
| std   |  13.6106  |
| min   |   2.48    |
| 25%   |   7.12875 |
| 50%   |  12.635   |
| 75%   |  20.425   |
| max   | 106.2     |

</div>


![R.LTWB](Graph/Plot_Q_MEDIA_M_28017120_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28017120_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28017120_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28017120_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: CAIMANCITO [25027590] (339 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.571138889,-73.79472222) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.571138889&lon=-73.79472222)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion        |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25027590 | CAIMANCITO [25027590] |   9.57114 |   -73.7947 |        40 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Astrea      | 1974-07-15 00:00:00 | 2019-02-07 11:40:00 | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   54.68 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 339      |
| mean  |  53.8843 |
| std   |  39.6006 |
| min   |   0.723  |
| 25%   |  17.325  |
| 50%   |  44.15   |
| 75%   |  87.27   |
| max   | 158.1    |

</div>


![R.LTWB](Graph/Plot_Q_MEDIA_M_25027590_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027590_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027590_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027590_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: CHEMESQUEMENA [28017150] (52 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.71222222,-73.40222222) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.71222222&lon=-73.40222222)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion           |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 2017-06-01 00:00:00 |         28017150 | CHEMESQUEMENA [28017150] |   10.7122 |   -73.4022 |      1160 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 2014-01-10 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      | 7.90542 |       4 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 52       |
| mean  |  6.36198 |
| std   |  3.45506 |
| min   |  1.67986 |
| 25%   |  3.65216 |
| 50%   |  6.36845 |
| 75%   |  7.92197 |
| max   | 15.2573  |

</div>


![R.LTWB](Graph/Plot_Q_MEDIA_M_28017150_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28017150_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28017150_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28017150_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: FLORES LAS [28027030] (439 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.09652778,-73.24352778) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.09652778&lon=-73.24352778)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion        |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28027030 | FLORES LAS [28027030] |   10.0965 |   -73.2435 |       112 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | La Paz      | 1962-10-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   2.045 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |     Valor |
|:------|----------:|
| count | 439       |
| mean  |   4.1023  |
| std   |   6.57997 |
| min   |   0       |
| 25%   |   0.815   |
| 50%   |   2.055   |
| 75%   |   5.4085  |
| max   |  95.94    |

</div>


![R.LTWB](Graph/Plot_Q_MEDIA_M_28027030_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28027030_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28027030_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28027030_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: GRACIAS A DIOS HACIENDA [25027080] (449 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.194472222,-73.57652778) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.194472222&lon=-73.57652778)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion                     |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-----------------------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25027080 | GRACIAS A DIOS HACIENDA [25027080] |   9.19447 |   -73.5765 |        46 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Curumaní    | 1963-07-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   2.381 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |     Valor |
|:------|----------:|
| count | 449       |
| mean  |   4.61716 |
| std   |   7.4523  |
| min   |   0.018   |
| 25%   |   0.8775  |
| 50%   |   1.999   |
| 75%   |   4.948   |
| max   |  73.81    |

</div>


![R.LTWB](Graph/Plot_Q_MEDIA_M_25027080_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027080_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027080_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027080_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: MATILDE LA [28027020] (399 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.16561111,-73.25833333) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.16561111&lon=-73.25833333)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion        |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28027020 | MATILDE LA [28027020] |   10.1656 |   -73.2583 |       114 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | San Diego   | 1962-07-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   1.363 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |     Valor |
|:------|----------:|
| count | 399       |
| mean  |   2.40145 |
| std   |   2.89938 |
| min   |   0       |
| 25%   |   0.4485  |
| 50%   |   1.3     |
| 75%   |   3.4115  |
| max   |  17.66    |

</div>


![R.LTWB](Graph/Plot_Q_MEDIA_M_28027020_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28027020_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28027020_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28027020_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: MINA LA [28017110] (465 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.68672222,-73.26983333) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.68672222&lon=-73.26983333)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion     |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28017110 | MINA LA [28017110] |   10.6867 |   -73.2698 |       429 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1969-12-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   3.582 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |     Valor |
|:------|----------:|
| count | 465       |
| mean  |   9.51238 |
| std   |  12.7092  |
| min   |   0.118   |
| 25%   |   3.361   |
| 50%   |   5.64    |
| 75%   |  10.0068  |
| max   | 116.79    |

</div>


![R.LTWB](Graph/Plot_Q_MEDIA_M_28017110_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28017110_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28017110_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28017110_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: PUENTE CARRETERA [25027890] (424 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.342333333,-73.49088889) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.342333333&lon=-73.49088889)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion              |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25027890 | PUENTE CARRETERA [25027890] |   9.34233 |   -73.4909 |       120 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Chiriguaná  | 1978-09-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   1.176 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |     Valor |
|:------|----------:|
| count | 424       |
| mean  |   2.66422 |
| std   |   3.14918 |
| min   |   0.007   |
| 25%   |   0.5025  |
| 50%   |   1.33    |
| 75%   |   3.70275 |
| max   |  18.55    |

</div>


![R.LTWB](Graph/Plot_Q_MEDIA_M_25027890_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027890_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027890_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027890_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: REPOSO EL [28017050] (263 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.52719444,-73.33636111) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.52719444&lon=-73.33636111)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28017050 | REPOSO EL [28017050] |   10.5272 |   -73.3364 |       350 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1958-03-15 00:00:00 | 2019-02-07 11:41:00 | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   9.391 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 263      |
| mean  |  20.0189 |
| std   |  28.2952 |
| min   |   3      |
| 25%   |   7.33   |
| 50%   |  13.44   |
| 75%   |  22.74   |
| max   | 252      |

</div>


![R.LTWB](Graph/Plot_Q_MEDIA_M_28017050_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28017050_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28017050_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28017050_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: SANTA TERESA [28027040] (412 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.915944444,-73.28369444) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.915944444&lon=-73.28369444)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion          |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28027040 | SANTA TERESA [28027040] |   9.91594 |   -73.2837 |        80 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Becerrill   | 1962-11-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   0.944 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |       Valor |
|:------|------------:|
| count | 412         |
| mean  |   3.04977   |
| std   |   4.03069   |
| min   |   0.0190909 |
| 25%   |   0.67875   |
| 50%   |   1.585     |
| 75%   |   3.8395    |
| max   |  44         |

</div>


![R.LTWB](Graph/Plot_Q_MEDIA_M_28027040_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28027040_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28027040_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28027040_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: BECERRIL [28027050] (349 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.686611111,-73.27919444) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.686611111&lon=-73.27919444)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion      |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado | Calificador    |   NivelAprobacion |
|:--------------------|-----------------:|:--------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|:---------------|------------------:|
| 1980-01-01 00:00:00 |         28027050 | BECERRIL [28027050] |   9.68661 |   -73.2792 |       106 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Becerrill   | 1963-06-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |    1.28 |       4 | EST. REGRESION |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 349      |
| mean  |  11.311  |
| std   |  22.5481 |
| min   |   0.161  |
| 25%   |   1.625  |
| 50%   |   4.267  |
| 75%   |  10.11   |
| max   | 294.1    |

</div>


![R.LTWB](Graph/Plot_Q_MEDIA_M_28027050_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28027050_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28027050_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28027050_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: CANTACLARO [28037060] (482 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.08847222,-73.73280556) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.08847222&lon=-73.73280556)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion        |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28037060 | CANTACLARO [28037060] |   10.0885 |   -73.7328 |       120 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1963-03-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   0.531 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |     Valor |
|:------|----------:|
| count | 482       |
| mean  |   1.77203 |
| std   |   2.00638 |
| min   |   0.03    |
| 25%   |   0.5315  |
| 50%   |   1.04342 |
| 75%   |   2.36855 |
| max   |  17.87    |

</div>


![R.LTWB](Graph/Plot_Q_MEDIA_M_28037060_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28037060_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28037060_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28037060_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: CONVENCION HACIENDA [28037020] (362 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.26783333,-73.41713889) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.26783333&lon=-73.41713889)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion                 |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28037020 | CONVENCION HACIENDA [28037020] |   10.2678 |   -73.4171 |       104 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1962-12-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   2.411 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |     Valor |
|:------|----------:|
| count | 362       |
| mean  |   2.65542 |
| std   |   3.09609 |
| min   |   0       |
| 25%   |   0.444   |
| 50%   |   1.469   |
| 75%   |   3.7135  |
| max   |  20.24    |

</div>


![R.LTWB](Graph/Plot_Q_MEDIA_M_28037020_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28037020_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28037020_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28037020_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: ISLANDIA [28027160] (372 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.632527778,-73.63572222) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.632527778&lon=-73.63572222)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion      |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:--------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28027160 | ISLANDIA [28027160] |   9.63253 |   -73.6357 |        45 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | El Paso     | 1974-11-15 00:00:00 | 2019-02-07 11:40:00 | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   3.109 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |     Valor |
|:------|----------:|
| count | 372       |
| mean  |   8.80949 |
| std   |   8.92743 |
| min   |   0.013   |
| 25%   |   2.68175 |
| 50%   |   6.026   |
| 75%   |  12.655   |
| max   |  69.15    |

</div>


![R.LTWB](Graph/Plot_Q_MEDIA_M_28027160_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28027160_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28027160_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28027160_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: MARIANGOLA [28037040] (474 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.18741667,-73.58519444) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.18741667&lon=-73.58519444)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion        |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28037040 | MARIANGOLA [28037040] |   10.1874 |   -73.5852 |        90 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1963-01-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   0.564 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |      Valor |
|:------|-----------:|
| count | 474        |
| mean  |   1.99652  |
| std   |   2.4448   |
| min   |   0.01     |
| 25%   |   0.367828 |
| 50%   |   1.01634  |
| 75%   |   2.6945   |
| max   |  13.28     |

</div>


![R.LTWB](Graph/Plot_Q_MEDIA_M_28037040_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28037040_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28037040_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28037040_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: PUEBLO BELLO [28047020] (474 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.41984722,-73.58883333) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.41984722&lon=-73.58883333)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion          |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio    | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:-------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28047020 | PUEBLO BELLO [28047020] |   10.4198 |   -73.5888 |      1125 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Pueblo Bello | 1963-01-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   1.224 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |      Valor |
|:------|-----------:|
| count | 474        |
| mean  |   1.28277  |
| std   |   0.950413 |
| min   |   0.244    |
| 25%   |   0.658511 |
| 50%   |   1.03365  |
| 75%   |   1.539    |
| max   |   6.531    |

</div>


![R.LTWB](Graph/Plot_Q_MEDIA_M_28047020_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28047020_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28047020_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28047020_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: PUENTE CALLAO [28037010] (437 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.36288889,-73.31736111) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.36288889&lon=-73.31736111)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion           |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28037010 | PUENTE CALLAO [28037010] |   10.3629 |   -73.3174 |       120 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1962-12-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   0.424 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |     Valor |
|:------|----------:|
| count | 437       |
| mean  |   3.03674 |
| std   |   4.55045 |
| min   |   0.009   |
| 25%   |   0.34    |
| 50%   |   1.402   |
| 75%   |   3.684   |
| max   |  30.45    |

</div>


![R.LTWB](Graph/Plot_Q_MEDIA_M_28037010_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28037010_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28037010_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28037010_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: PUENTE CANOAS  - AUT [28037090] (410 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.646333333,-73.65183333) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.646333333&lon=-73.65183333)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion                  |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:--------------------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28037090 | PUENTE CANOAS  - AUT [28037090] |   9.64633 |   -73.6518 |        45 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | El Paso     | 1965-04-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   30.47 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |       Valor |
|:------|------------:|
| count | 410         |
| mean  |  56.379     |
| std   |  51.3416    |
| min   |   0.0106789 |
| 25%   |  12.65      |
| 50%   |  41.18      |
| 75%   |  90.1875    |
| max   | 209.741     |

</div>


![R.LTWB](Graph/Plot_Q_MEDIA_M_28037090_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28037090_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28037090_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28037090_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: PUENTE CARRETERA [28037130] (422 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.15752778,-73.62477778) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.15752778&lon=-73.62477778)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion              |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28037130 | PUENTE CARRETERA [28037130] |   10.1575 |   -73.6248 |        80 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1972-10-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   0.899 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |       Valor |
|:------|------------:|
| count | 422         |
| mean  |   4.41579   |
| std   |   5.69845   |
| min   |   0.0140806 |
| 25%   |   0.944     |
| 50%   |   2.01      |
| 75%   |   5.36175   |
| max   |  35.46      |

</div>


![R.LTWB](Graph/Plot_Q_MEDIA_M_28037130_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28037130_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28037130_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28037130_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: PUENTE SALGUERO  - AUT [28037030] (474 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.38411111,-73.23247222) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.38411111&lon=-73.23247222)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion                    |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28037030 | PUENTE SALGUERO  - AUT [28037030] |   10.3841 |   -73.2325 |       113 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1962-12-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   16.16 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 474      |
| mean  |  33.6422 |
| std   |  38.3711 |
| min   |   1.221  |
| 25%   |   7.753  |
| 50%   |  20.465  |
| 75%   |  41.5703 |
| max   | 232.8    |

</div>


![R.LTWB](Graph/Plot_Q_MEDIA_M_28037030_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28037030_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28037030_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28037030_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: BELLEZA LA [28047080] (96 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.33333333,-73.95) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.33333333&lon=-73.95)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion        |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado | Calificador    |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|:---------------|------------------:|
| 1982-01-01 00:00:00 |         28047080 | BELLEZA LA [28047080] |   10.3333 |     -73.95 |       250 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | El Copey    | 1982-06-15 00:00:00 | 1992-09-15 00:00:00 | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |    13.8 |       4 | EST. REGRESION |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 96       |
| mean  | 16.3821  |
| std   |  6.47651 |
| min   |  6.365   |
| 25%   | 11.7875  |
| 50%   | 15.865   |
| 75%   | 18.8225  |
| max   | 47.38    |

</div>


![R.LTWB](Graph/Plot_Q_MEDIA_M_28047080_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28047080_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28047080_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28047080_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: PUENTE CARRETERA [28047040] (247 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.271,-73.97266667) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.271&lon=-73.97266667)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion              |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28047040 | PUENTE CARRETERA [28047040] |    10.271 |   -73.9727 |       151 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | El Copey    | 1963-02-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |    1.46 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |     Valor |
|:------|----------:|
| count | 247       |
| mean  |   2.64994 |
| std   |   2.25132 |
| min   |   0.25    |
| 25%   |   1.2385  |
| 50%   |   1.997   |
| 75%   |   3.318   |
| max   |  13.65    |

</div>


![R.LTWB](Graph/Plot_Q_MEDIA_M_28047040_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28047040_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28047040_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28047040_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: CARACOLI - AUT [15067210] (28 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.95011111,-73.05102778) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.95011111&lon=-73.05102778)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion            |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio          | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:--------------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:-------------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 2012-04-01 00:00:00 |         15067210 | CARACOLI - AUT [15067210] |   10.9501 |    -73.051 |       460 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | San Juan Del Cesar | 2011-01-12 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   8.695 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 28       |
| mean  |  5.99268 |
| std   |  4.02808 |
| min   |  1.51655 |
| 25%   |  3.0025  |
| 50%   |  4.716   |
| 75%   |  8.31065 |
| max   | 17.14    |

</div>


![R.LTWB](Graph/Plot_Q_MEDIA_M_15067210_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_15067210_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_15067210_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_15067210_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: CERCADO EL-AUTOMAT [15067020] (328 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.9075,-73.00833333) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.9075&lon=-73.00833333)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion                |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         15067020 | CERCADO EL-AUTOMAT [15067020] |   10.9075 |   -73.0083 |       335 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | Fonseca     | 2004-04-09 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |    6.81 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |     Valor |
|:------|----------:|
| count | 328       |
| mean  |   6.88666 |
| std   |   4.37317 |
| min   |   1.114   |
| 25%   |   3.963   |
| 50%   |   5.5075  |
| 75%   |   8.558   |
| max   |  27.85    |

</div>


![R.LTWB](Graph/Plot_Q_MEDIA_M_15067020_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_15067020_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_15067020_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_15067020_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: CORRAL DE PIEDRA [28017080] (465 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.81891667,-73.05508333) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.81891667&lon=-73.05508333)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion              |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio          | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:-------------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28017080 | CORRAL DE PIEDRA [28017080] |   10.8189 |   -73.0551 |       275 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | San Juan Del Cesar | 1970-03-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   0.865 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |       Valor |
|:------|------------:|
| count | 465         |
| mean  |   2.49671   |
| std   |   3.54568   |
| min   |   0.0238819 |
| 25%   |   0.606     |
| 50%   |   1.13      |
| 75%   |   2.725     |
| max   |  22.94      |

</div>


![R.LTWB](Graph/Plot_Q_MEDIA_M_28017080_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28017080_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28017080_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28017080_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: EL SILENCIO - AUT [15067200] (115 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.91708333,-72.91533333) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.91708333&lon=-72.91533333)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion               |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-----------------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 2010-06-01 00:00:00 |         15067200 | EL SILENCIO - AUT [15067200] |   10.9171 |   -72.9153 |       255 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | Fonseca     | 2010-06-25 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   6.725 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |     Valor |
|:------|----------:|
| count | 115       |
| mean  |   7.45147 |
| std   |   7.71757 |
| min   |   1.019   |
| 25%   |   2.61302 |
| 50%   |   4.30484 |
| 75%   |   9.2741  |
| max   |  38.9706  |

</div>


![R.LTWB](Graph/Plot_Q_MEDIA_M_15067200_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_15067200_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_15067200_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_15067200_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: MAGUEYES LOS [15067080] (291 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.94672222,-72.77227778) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.94672222&lon=-72.77227778)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion          |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-07-01 00:00:00 |         15067080 | MAGUEYES LOS [15067080] |   10.9467 |   -72.7723 |       140 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | Barrancas   | 1980-07-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   0.544 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |      Valor |
|:------|-----------:|
| count | 291        |
| mean  |   2.17867  |
| std   |   3.43166  |
| min   |   0.124    |
| 25%   |   0.575597 |
| 50%   |   0.977419 |
| 75%   |   2.45689  |
| max   |  31.85     |

</div>


![R.LTWB](Graph/Plot_Q_MEDIA_M_15067080_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_15067080_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_15067080_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_15067080_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: POZO HONDO [15067130] (388 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.99855556,-72.81955556) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.99855556&lon=-72.81955556)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion        |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1987-08-01 00:00:00 |         15067130 | POZO HONDO [15067130] |   10.9986 |   -72.8196 |       210 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | Barrancas   | 1987-07-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |    0.12 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |       Valor |
|:------|------------:|
| count | 388         |
| mean  |   0.107405  |
| std   |   0.156455  |
| min   |   0.002     |
| 25%   |   0.016     |
| 50%   |   0.0363357 |
| 75%   |   0.125     |
| max   |   0.936     |

</div>


![R.LTWB](Graph/Plot_Q_MEDIA_M_15067130_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_15067130_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_15067130_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_15067130_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: PUENTE GUAJIRO - AUT [15067150] (148 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.92644444,-72.80438889) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.92644444&lon=-72.80438889)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion                  |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:--------------------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 2008-11-01 00:00:00 |         15067150 | PUENTE GUAJIRO - AUT [15067150] |   10.9264 |   -72.8044 |       485 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | Barrancas   | 2008-07-22 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |      25 |       4 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |       Valor |
|:------|------------:|
| count | 148         |
| mean  |   5.06216   |
| std   |   5.59392   |
| min   |   0.0811156 |
| 25%   |   1.54901   |
| 50%   |   2.6945    |
| 75%   |   6.2928    |
| max   |  25.5854    |

</div>


![R.LTWB](Graph/Plot_Q_MEDIA_M_15067150_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_15067150_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_15067150_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_15067150_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: SAN FRANCISCO [15067170] (156 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.99122222,-72.75608333) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.99122222&lon=-72.75608333)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion           |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 2008-12-01 00:00:00 |         15067170 | SAN FRANCISCO [15067170] |   10.9912 |   -72.7561 |       450 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | Barrancas   | 2008-07-22 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   10.19 |       4 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |     Valor |
|:------|----------:|
| count | 156       |
| mean  |   9.50479 |
| std   |  12.6864  |
| min   |   0.516   |
| 25%   |   2.53293 |
| 50%   |   4.73477 |
| 75%   |  10.7563  |
| max   |  71.51    |

</div>


![R.LTWB](Graph/Plot_Q_MEDIA_M_15067170_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_15067170_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_15067170_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_15067170_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: CORRAL DE PIEDRA  - AUT [28017140] (41 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.83,-73.07) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.83&lon=-73.07)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion                     |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio          | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-----------------------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:-------------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 2010-01-01 00:00:00 |         28017140 | CORRAL DE PIEDRA  - AUT [28017140] |     10.83 |     -73.07 |       275 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | San Juan Del Cesar | 2004-09-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   76114 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |     Valor |
|:------|----------:|
| count |    41     |
| mean  | 18933.9   |
| std   | 23607.6   |
| min   |     0.562 |
| 25%   |     1.504 |
| 50%   |     3.513 |
| 75%   | 32296     |
| max   | 76114     |

</div>


![R.LTWB](Graph/Plot_Q_MEDIA_M_28017140_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28017140_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28017140_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28017140_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: AURORA LA [28047010] (412 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.27686111,-73.97780556) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.27686111&lon=-73.97780556)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28047010 | AURORA LA [28047010] |   10.2769 |   -73.9778 |       150 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Fundación   | 1961-05-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   16.83 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |     Valor |
|:------|----------:|
| count | 412       |
| mean  |  16.1567  |
| std   |   8.49034 |
| min   |   0.625   |
| 25%   |  11.3293  |
| 50%   |  14.845   |
| 75%   |  19.2775  |
| max   |  65.28    |

</div>


![R.LTWB](Graph/Plot_Q_MEDIA_M_28047010_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28047010_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28047010_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28047010_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: CANAL FLORIDA [29067050] (393 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.75886111,-74.10663889) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.75886111&lon=-74.10663889)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion           |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio     | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:--------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29067050 | CANAL FLORIDA [29067050] |   10.7589 |   -74.1066 |        60 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1965-05-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   7.816 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |     Valor |
|:------|----------:|
| count | 393       |
| mean  |  12.6539  |
| std   |   9.55028 |
| min   |   1.572   |
| 25%   |   6.14022 |
| 50%   |  10.8     |
| 75%   |  16.3514  |
| max   |  94.89    |

</div>


![R.LTWB](Graph/Plot_Q_MEDIA_M_29067050_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_29067050_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_29067050_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_29067050_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: EL BANCO - AUT [25027020] (504 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=8.992527778,-73.96944444) or [Openstreet Map](https://www.openstreetmap.org/query?lat=8.992527778&lon=-73.96944444)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion            |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:--------------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25027020 | EL BANCO - AUT [25027020] |   8.99253 |   -73.9694 |        29 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena      | El Banco    | 1934-01-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |    3231 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count |  504    |
| mean  | 4075.69 |
| std   | 1368.36 |
| min   | 1245.65 |
| 25%   | 3091.5  |
| 50%   | 3956.67 |
| 75%   | 4960.75 |
| max   | 9171    |

</div>


![R.LTWB](Graph/Plot_Q_MEDIA_M_25027020_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027020_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027020_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027020_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: FUNDACION [29067120] (444 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.52325,-74.18280556) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.52325&lon=-74.18280556)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29067120 | FUNDACION [29067120] |   10.5233 |   -74.1828 |        55 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Fundación   | 1958-04-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   21.44 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 444      |
| mean  |  28.2809 |
| std   |  18.1198 |
| min   |   4.831  |
| 25%   |  15.86   |
| 50%   |  24.445  |
| 75%   |  35.5075 |
| max   | 140.9    |

</div>


![R.LTWB](Graph/Plot_Q_MEDIA_M_29067120_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_29067120_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_29067120_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_29067120_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: PALMARIGUANI  - AUT [28047050] (451 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.930972222,-73.95880556) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.930972222&lon=-73.95880556)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion                 |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio             | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:----------------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28047050 | PALMARIGUANI  - AUT [28047050] |   9.93097 |   -73.9588 |        80 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Ariguaní (El Dificil) | 1978-10-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   10.28 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 451      |
| mean  |  13.5702 |
| std   |  13.6383 |
| min   |   0.127  |
| 25%   |   2.9885 |
| 50%   |   8.391  |
| 75%   |  20.35   |
| max   |  63.14   |

</div>


![R.LTWB](Graph/Plot_Q_MEDIA_M_28047050_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28047050_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28047050_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28047050_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: PUERTO RICO HACIENDA  - AUT [29067060] (257 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.5,-74.13333333) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.5&lon=-74.13333333)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion                         |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29067060 | PUERTO RICO HACIENDA  - AUT [29067060] |      10.5 |   -74.1333 |        55 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Aracataca   | 1967-06-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   17.88 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 257      |
| mean  |  24.8152 |
| std   |  12.422  |
| min   |   4.068  |
| 25%   |  15.44   |
| 50%   |  22.37   |
| 75%   |  32.55   |
| max   |  88.67   |

</div>


![R.LTWB](Graph/Plot_Q_MEDIA_M_29067060_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_29067060_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_29067060_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_29067060_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: RIO FRIO [29067070] (426 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.90541667,-74.15411111) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.90541667&lon=-74.15411111)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion      |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:--------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29067070 | RIO FRIO [29067070] |   10.9054 |   -74.1541 |        30 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Ciénaga     | 1978-07-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   7.213 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |     Valor |
|:------|----------:|
| count | 426       |
| mean  |  13.4932  |
| std   |   9.06389 |
| min   |   2.06    |
| 25%   |   6.24475 |
| 50%   |  11.37    |
| 75%   |  18.18    |
| max   |  59.47    |

</div>


![R.LTWB](Graph/Plot_Q_MEDIA_M_29067070_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_29067070_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_29067070_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_29067070_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: SANTA ROSALIA [29067040] (446 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.83080556,-74.12055556) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.83080556&lon=-74.12055556)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion           |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio     | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:--------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29067040 | SANTA ROSALIA [29067040] |   10.8308 |   -74.1206 |        55 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1965-05-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   0.514 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |     Valor |
|:------|----------:|
| count | 446       |
| mean  |   1.91476 |
| std   |   1.48993 |
| min   |   0.106   |
| 25%   |   0.78925 |
| 50%   |   1.439   |
| 75%   |   2.73225 |
| max   |   7.354   |

</div>


![R.LTWB](Graph/Plot_Q_MEDIA_M_29067040_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_29067040_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_29067040_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_29067040_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: TREBOL EL [29067010] (448 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.63591667,-74.14633333) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.63591667&lon=-74.14633333)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado | Calificador    |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|:---------------|------------------:|
| 1980-01-01 00:00:00 |         29067010 | TREBOL EL [29067010] |   10.6359 |   -74.1463 |        60 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Ciénaga     | 1958-03-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   7.281 |       4 | EST. REGRESION |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |     Valor |
|:------|----------:|
| count | 448       |
| mean  |  17.5998  |
| std   |  11.6086  |
| min   |   2.966   |
| 25%   |   9.71225 |
| 50%   |  15.525   |
| 75%   |  21.6225  |
| max   | 119       |

</div>


![R.LTWB](Graph/Plot_Q_MEDIA_M_29067010_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_29067010_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_29067010_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_29067010_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: GANADERIA CARIBE  - AUT [29067150] (481 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.57491667,-74.12666667) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.57491667&lon=-74.12666667)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion                     |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-----------------------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29067150 | GANADERIA CARIBE  - AUT [29067150] |   10.5749 |   -74.1267 |        67 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Aracataca   | 1965-05-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   11.91 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |      Valor |
|:------|-----------:|
| count | 481        |
| mean  |  15.9357   |
| std   |   9.25158  |
| min   |   0.479067 |
| 25%   |   8.836    |
| 50%   |  14.42     |
| 75%   |  21.58     |
| max   |  55.25     |

</div>


![R.LTWB](Graph/Plot_Q_MEDIA_M_29067150_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_29067150_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_29067150_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_29067150_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: PUENTE FERROCARRIL [29067130] (476 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.58580556,-74.19211111) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.58580556&lon=-74.19211111)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion                |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29067130 | PUENTE FERROCARRIL [29067130] |   10.5858 |   -74.1921 |        37 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Aracataca   | 1965-05-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   7.851 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |     Valor |
|:------|----------:|
| count | 476       |
| mean  |  17.6187  |
| std   |  14.6576  |
| min   |   1.95487 |
| 25%   |   7.617   |
| 50%   |  13.59    |
| 75%   |  22.0241  |
| max   |  97.6     |

</div>


![R.LTWB](Graph/Plot_Q_MEDIA_M_29067130_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_29067130_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_29067130_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_29067130_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: PUENTE SEVILLA  - AUT [29067160] (397 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=10.79883333,-74.02858333) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.79883333&lon=-74.02858333)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion                   |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado | Calificador    |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|:---------------|------------------:|
| 1982-01-01 00:00:00 |         29067160 | PUENTE SEVILLA  - AUT [29067160] |   10.7988 |   -74.0286 |        10 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Ciénaga     | 1982-07-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   3.595 |       4 | EST. REGRESION |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |     Valor |
|:------|----------:|
| count | 397       |
| mean  |   7.71179 |
| std   |   8.21195 |
| min   |   0.546   |
| 25%   |   2.326   |
| 50%   |   5.185   |
| 75%   |  10.81    |
| max   |  71.7432  |

</div>


![R.LTWB](Graph/Plot_Q_MEDIA_M_29067160_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_29067160_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_29067160_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_29067160_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: CABLE EL [16067020] (244 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=8.676388889,-72.94972222) or [Openstreet Map](https://www.openstreetmap.org/query?lat=8.676388889&lon=-72.94972222)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion      |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                          | Departamento       | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:--------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:---------------------------------------|:-------------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         16067020 | CABLE EL [16067020] |   8.67639 |   -72.9497 |       110 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 08 - Santanderes-Arauca | Norte De Santander | El Tarra    | 1976-08-15 00:00:00 | 2001-04-20 00:00:00 | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   68.34 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 244      |
| mean  | 115.375  |
| std   |  66.9092 |
| min   |  28.67   |
| 25%   |  64.19   |
| 50%   |  95.225  |
| 75%   | 154.075  |
| max   | 340.3    |

</div>


![R.LTWB](Graph/Plot_Q_MEDIA_M_16067020_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_16067020_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_16067020_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_16067020_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: CAMPO SEIS [16037040] (387 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=8.601111111,-72.80861111) or [Openstreet Map](https://www.openstreetmap.org/query?lat=8.601111111&lon=-72.80861111)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion        |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                          | Departamento       | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado | Calificador        |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:---------------------------------------|:-------------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|:-------------------|------------------:|
| 1980-01-01 00:00:00 |         16037040 | CAMPO SEIS [16037040] |   8.60111 |   -72.8086 |        70 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 08 - Santanderes-Arauca | Norte De Santander | Tibú        | 1973-04-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   9.241 |       4 | EST. INTERPOLACION |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 387      |
| mean  |  21.8745 |
| std   |  17.4017 |
| min   |   3.445  |
| 25%   |  11.475  |
| 50%   |  16.64   |
| 75%   |  27.555  |
| max   | 208.9    |

</div>


![R.LTWB](Graph/Plot_Q_MEDIA_M_16037040_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_16037040_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_16037040_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_16037040_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: PUENTE TARRA [16047020] (283 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=8.588611111,-73.08111111) or [Openstreet Map](https://www.openstreetmap.org/query?lat=8.588611111&lon=-73.08111111)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion          |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                          | Departamento       | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:---------------------------------------|:-------------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         16047020 | PUENTE TARRA [16047020] |   8.58861 |   -73.0811 |       140 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 08 - Santanderes-Arauca | Norte De Santander | El Tarra    | 1971-11-15 00:00:00 | 2014-06-18 00:00:00 | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   32.22 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 283      |
| mean  |  54.4958 |
| std   |  36.5487 |
| min   |  10.16   |
| 25%   |  29.87   |
| 50%   |  42.16   |
| 75%   |  67.44   |
| max   | 237.6    |

</div>


![R.LTWB](Graph/Plot_Q_MEDIA_M_16047020_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_16047020_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_16047020_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_16047020_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: PUERTO BARCO-GABARRA - AUT [16067010] (397 rec.)**<br>Location over [Google Maps](http://maps.google.com/maps?q=9.003611111,-72.9) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.003611111&lon=-72.9)

</div>


Station first record

| Fecha               |   CodigoEstacion | NombreEstacion                        |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                          | Departamento       | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:--------------------------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:---------------------------------------|:-------------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         16067010 | PUERTO BARCO-GABARRA - AUT [16067010] |   9.00361 |      -72.9 |        19 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 08 - Santanderes-Arauca | Norte De Santander | Tibú        | 1969-08-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   149.3 |      50 |           nan |               900 |

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 397      |
| mean  | 249.957  |
| std   | 137.419  |
| min   |  43.6941 |
| 25%   | 134.3    |
| 50%   | 225.4    |
| 75%   | 335.5    |
| max   | 914.8    |

</div>


![R.LTWB](Graph/Plot_Q_MEDIA_M_16067010_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_16067010_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_16067010_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_16067010_DensityKDE.png)
