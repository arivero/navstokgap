---
title: "Continuidad, composición, movimiento y medición — nota unificada de referencias históricas"
subtitle: "Fusión deduplicada de S1–S5 (chat «Confirmar referencias citadas» + dos informes de investigación)"
date: "2026-09-11"
lang: es
---

# 0. Procedencia, deduplicación y convenciones

## 0.1 Archivos de entrada

| Sigla | Archivo(s) | Contenido | Tratamiento |
|:--|:----------|:-------------------|:--------|
| **S1** | `ref1-4.pdf` (pp. 1–4 de 12) | Chat «cosas alex – Confirmar referencias citadas», turno 1. Petición: «locate and confirm all this references» sobre un transcript del repositorio pegado en markdown. Verifica 21 referencias (tabla de 21 filas) y propone correcciones. | Integrado. Columna «Veredicto» cortada por el margen derecho (§0.3). |
| **S2** | `ref4-end` (pp. 3–7 de 13) | Turno 2. Petición: «expand with the same technique, first remember from your weights, then search and confirm». 16 candidatos verificados (tabla de 16 filas) y conexiones. | Integrado. Tercera columna cortada. |
| **S3** | `ref4-end` (pp. 7–11) | Turno 3. Petición: «do other pass, excentrical». 14 candidatos (tabla de 14 filas) y conexiones. | Integrado. Tercera columna cortada. |
| **S4** | `deep-research-report.md` = `deep-research-report__2_.md`; `Investigacio_n_avanzada.pdf` | Informe «Investigación avanzada» (en el chat: 9 min, 43 citas, 975 búsquedas). Los dos `.md` son idénticos byte a byte. El PDF (31 pp.) es el mismo texto con notas 1–66 que resuelven a URL; el `.md` las sustituye por marcadores internos `cite…turn…` no resolubles. | Integrado. Notas del PDF resueltas en Anexo A y en `aux_trazabilidad.md` §4. |
| **S5** | `Investigacion_avanzada.md` (ES); `Advanced_research_report.md` (EN) | Segundo informe (15 min, 7 citas, 321 búsquedas), pedido como versión inglesa y con el pasaje de los sentidos del *Heart Sūtra* como vínculo con TTC 14. ES y EN son el mismo texto. | Integrado. EN tratado como duplicado de ES; variantes en §9 (D19). |
| — | `ref4-end` (pp. 12–13) | Arranque de ambos informes, petición del informe inglés, corrección de enlaces de descarga. | Solo procedencia. |

URL del chat: <https://chatgpt.com/g/g-p-69a9afaaf94481918fd7307bfa3bc4e4-cosas-alex/c/6aa337c8-a558-83eb-987b-3d2cc4d4c1a4>. Hashes MD5 e inventario completo: `aux_trazabilidad.md` §1.

## 0.2 Convenciones

| Elemento | Uso en esta nota |
|:--|:-------------|
| E01–E59 | Identificador de entrada (fichas en §3; índice en §2). |
| Estado | Vocabulario de S4. **Confirmado**: pasaje identificable comprobado en texto primario, testimonio antiguo o edición/traducción académica fiable. **Parcial**: obra y argumento reales, falta *pinpoint* primario satisfactorio o la edición abierta es secundaria. **Mislocated / no sustentado**: la referencia existe pero no prueba lo que se le hacía probar. S1 usa además «Confirmado directamente», «Confirmado bibliográficamente», «Referencia real y localizada», «Contenido confirmado, pero…». |
| Etiquetas S5 | `PRIMARY EXACT`, `PRIMARY INDIRECT`, `SECONDARY CONFIRMED`, `UNSPECIFIED`. S5 solo asigna una (`UNSPECIFIED`, Thābit). Las fuentes no definen equivalencia con el vocabulario de S4; no se mapea. |
| *pin* | Localización a nivel de pasaje (verso, página, folio, número de párrafo). |
| […] | Texto perdido por truncamiento en la fuente. Los fragmentos visibles literales están en `aux_trazabilidad.md` §3. |
| Fórmulas | Notación Unicode en lugar del LaTeX y los diagramas Mermaid de S4/S5. Contenido sin cambios; los diagramas se dan como tablas de aristas. |
| Ejes (§5) | C contacto/continuidad · M movimiento desde puntos/registros · S medición, equilibrio y secciones · B mereología y *binding* · R epistemología de registros · P propiedades intrínsecas/adventicias · G geometría estática frente a generación dinámica. |

## 0.3 Pérdidas en las fuentes

| Fuente | Pérdida | Tratamiento |
|:--|:------------|:------------|
| S1 | Columna «Veredicto» cortada (≈35–45 caracteres visibles por línea). El texto fuera de la caja de página no existe en el PDF (comprobado: ningún glifo más allá de x ≈ 572 pt). | Estado y sentido reconstruible en cada ficha; literal en aux §3.1. |
| S2 | Columna «Valor para nuestro tema» cortada; una fórmula desplegada cortada. | Paráfrasis en fichas; literal en aux §3.2. |
| S3 | Columna «Por qué me parece interesante aquí» cortada; dos fórmulas cortadas. | Ídem, aux §3.3. |
| S1–S3 | Chips de fuente «+1», «+2», «+3»: solo el primer enlace está en el PDF. | Enlaces recuperados: Anexo A. Etiquetas de chips con enlaces ocultos: aux §2. |
| S4 (.md) | Marcadores `cite…turn…` sin URL. | Resueltos con las notas del PDF (aux §4). |
| S5 | El mensaje de entrega en el chat anuncia «tres columnas de relevancia Mereología / Geometría-topología / Dinámica-medición», «tablas de atribuciones problemáticas» y «diagramas Mermaid». No están en los `.md` entregados. | Registrado (D20). No recuperable. |

# 1. Estructura conceptual

## 1.1 Familias de problemas

S4 identifica cinco familias; S5 cuatro problemas (S5 no separa la familia 4 de la 1).

| Nº | Problema | Formulación | Fuentes representativas | Origen |
|:--|:----------|:-----------|:-----------|:--|
| 1 | Cómo pueden ponerse en contacto indivisibles | co-localización ≠ contacto ≠ contigüidad ≠ composición | Aristóteles, Mohistas, Nyāya, Jainismo, Vasubandhu, Ibn Sīnā | S4, S5 §1.1 |
| 2 | Cómo una sucesión de posiciones constituye o representa movimiento; generación frente a constitución | procedimiento de generación ≠ constitución del objeto | Proclo, al-Rāzī, Galileo; Nāgārjuna, Ṭūsī | S4, S5 §1.2 |
| 3 | Cómo registros o secciones de menor dimensión determinan un objeto global | familia de secciones ⇒ determinación global, sin afirmar que el objeto esté compuesto de esas secciones | Arquímedes, Liu Hui, Zu Geng, Cavalieri | S4, S5 §1.3, S2 |
| 4 | Qué relación adicional convierte partes próximas en un compuesto | co-ubicación ≠ *binding* | *Tattvārthasūtra*, *Mohist Canon* A2/A61/A69, Nyāya *avayavin* | S4, S3 |
| 5 | Diferencia entre la causa de una observación y el objeto que representa | causa física del registro ≠ objeto representado | Dignāga, *Mohist Canon* B17 | S4, S5 §1.4 |

El transcript original del repositorio ya convergía hacia la distinción entre estructura estática, composición, medida y dinámica (S4, remitiendo al transcript pegado).

Núcleos que la verificación refuerza (S4): Aristóteles *Physics* VI.1 (continuo no compuesto de indivisibles); Vasubandhu y Nyāya (qué significa que un átomo tenga contactos espacialmente distintos); Mohistas (teoría positiva del extremo sin espesor y de la contigüidad); al-Rāzī (puntos sucesivos de contacto de una esfera rodante → composición puntual de la línea); Thābit (estática del equilibrio y la balanza); Ṭūsī (trayectoria lineal observada desde estructura cinemática circular latente).

## 1.2 Formulaciones y conexiones propuestas en las pasadas

| Nº | Formulación | Fuentes históricas implicadas | Origen |
|:--|:----------------|:----------|:--|
| F1 | Triángulo de respuestas al contacto: (a) un continuo no puede componerse de indivisibles sin partes; (b) un átomo sin partes con contacto localizado parece adquirir partes, y Nyāya lo salva con conjunción y fin de la regresión; (c) un límite sin magnitud cumple una función positiva: define contigüidad sin solapamiento. | Aristóteles; Vasubandhu/Nyāya; Mohistas | S2 |
| F2 | «¿Pueden los simples componer lo extenso?» es demasiado grueso: separar constituyentes ≠ límites ≠ relaciones de contigüidad. Un objeto extenso no tiene por qué estar hecho de sus puntos frontera para que esos puntos sean esenciales a la estructura que hace posible su composición. | Mohistas A61/A69 | S2 |
| F3 | punto —(movimiento)→ línea. Proclo: generación, no esencia. al-Rāzī: inferencia inversa, la línea se compone de los puntos de contacto. Galileo: trayectoria de infinitos contactos → estructura del continuo. | Proclo, al-Rāzī, Galileo | S2 |
| F4 | contacto estático → registros sucesivos → trayectoria (S2); contacto estático → sucesión de registros → continuo espacial (S5). La disputa: qué se puede inferir sobre la ontología del continuo a partir de la secuencia de registros. | al-Rāzī (S5); Proclo, al-Rāzī, Galileo (S2) | S2, S5 |
| F5 | Arquímedes / Liu Hui–Zu Geng / Cavalieri ⇒ objeto global determinado por una familia exhaustiva [de secciones] (fórmula cortada en S2). Preguntas: (i) ¿qué familia mínima de registros estáticos determina un estado global?; (ii) ¿qué compatibilidad entre registros garantiza que proceden de un único objeto? Conecta *Mohist* A69, Nyāya *avayavin*, Cavalieri y la distinción previa entre estructura de medida a tiempo fijo y ley dinámica. | Arquímedes, Liu Hui, Zu Geng, Cavalieri | S2 |
| F6 | atom count ≢ spatial occupancy; co-location ≢ binding; y una estructura que permite movimiento/reposo sin producirlo dinámicamente. De ahí: mereology / geometry / dynamics como tres estructuras. Que A y B sean partes distintas, estén en lugares distintos y puedan evolucionar independientemente son tres afirmaciones diferentes; el error recurrente de varios argumentos atomistas antiguos es identificar dos de ellas. | *Tattvārthasūtra* | S3; S5 §2 (mereología ≠ geometría ≠ dinámica) |
| F7 | Bloque jaina 5.11–17 + 5.33 ss.: átomos indivisibles; varios átomos pueden compartir posición; compartir posición no los hace compuesto; hay una regla adicional de *binding*; hay medios continuos de movimiento/reposo que no son fuerzas. Arquitectura: degrees of freedom + occupancy map + compatibility relation + kinematic background. S3 lo sitúa por delante de al-Rāzī como hallazgo a desarrollar. | *Tattvārthasūtra* | S3 |
| F8 | physical cause —M→ record —R→ quantity inferred. La pregunta del transcript «what makes a measured effect belong to an object rather than to the apparatus?» se reformula como «¿qué propiedades del objeto son invariantes bajo cambios admisibles del prot[ocolo…]?» (cortado). | Dignāga, Heytesbury, Takebe | S3 |
| F9 | ¿Qué invariantes entre registros autorizan a atribuirlos al mismo objeto? | Dignāga, *Mohist* B17 | S5 §1.4 |
| F10 | Khayyām: no meter movimiento en geometría / al-Qūhī–al-Sijzī: definir o clasificar por generación mediante movimiento; debajo, Abū al-Barakāt: ¿el movimiento reconstruido desde posiciones es realidad del mundo o síntesis del observador? Corresponde a la separación fixed-time structure / law-history of evolution. | Khayyām, al-Qūhī, al-Sijzī, Abū al-Barakāt | S3 |
| F11 | No inferir la estructura estática del espacio desde un mecanismo dinámico de generación (importado). | Khayyām | S5 |
| F12 | ¿Una trayectoria es solo reconstrucción de registros o existe sucesión adicional en el mundo? | Abū al-Barakāt | S5 |
| F13 | Choose the discretisation that preserves the structure you are trying to infer. S3 lo relaciona con el trabajo del usuario sobre Navier–Stokes/measurement. | Takebe | S3, S5 |
| F14 | configuración estática + ley de equilibrio + procedimiento de lectura → cantidad inferida. Un aparato no es solo algo que da un número: hay una clase de configuraciones admisibles (equilibrio) dentro de la cual la lectura cuenta como medida. Precedente para el *measurement layer*. | Thābit | S4 |
| F15 | movimiento aparente del cielo ⇏ movimiento del cielo. Una historia observacional admite otra asignación de movimiento si cambia el marco de interpretación. La comparación con *identifiability* es inferencia nuestra, no vocabulario de Hong. | Hong Dae-yong | S4 |
| F16 | registro cinemático simple ⇏ dinámica latente simple (S5); `recorded trajectory = unique dynamics` es falso (S4). | Ṭūsī | S4, S5 |
| F17 | Parts ≠ locations ≠ contacts ≠ binding ≠ records ≠ dynamics. Fuentes que rompen identificaciones: Jainismo (pluralidad mereológica no determina ocupación; co-ubicación no determina *binding*); Ṭūsī (trayectoria registrada ≠ dinámica única); Thābit (medida de peso con sentido solo dentro de condiciones de equilibrio). | Jainismo, Ṭūsī, Thābit | S4 |
| F18 | referencia existente ≠ referencia relevante. | Aquinas SCG III.64–77 | S4 |

## 1.3 Puente con el programa (diagrama de S4 como tabla de aristas)

| Origen | Relación | Destino |
|:----------|:----------|:----------|
| Partes / grados de libertad | → | Geometría y ocupación |
| Geometría y ocupación | → | Compatibilidad / contacto |
| Compatibilidad / contacto | → | *Binding*: qué constituye un objeto |
| *Binding* | → | Estado estático |
| Estado estático | → | Interacción de medida |
| Interacción de medida | → | Registro |
| Estado estático | → | Ley dinámica |
| Ley dinámica | → | Historia / trayectoria inferida |
| Registro | impone restricciones sobre (línea discontinua) | Historia / trayectoria inferida |
| Registro | no identifica por sí solo (línea discontinua) | Ley dinámica |

## 1.4 Síntesis final de S4

El corpus no se presenta bajo la rúbrica «antiguas ideas sobre átomos». Documenta: (1) cómo se constituye un todo a partir de relaciones locales; (2) qué información puede obtenerse de sus secciones o estados estáticos; (3) qué hace que una lectura pertenezca al objeto y no solo al aparato; (4) cuándo una secuencia de registros determina, o no, una dinámica.

Asignación por fuente: Aristóteles, Vasubandhu y Nyāya fijan el problema de contacto; Mohistas y Jainismo separan frontera, localización y composición; Liu Hui, Zu Geng, Arquímedes y Cavalieri, secciones y aproximaciones; Thābit, equilibrio como condición de lectura; Dignāga, causa frente a objeto representado; al-Rāzī y Proclo, generación dinámica frente a constitución geométrica; Ṭūsī, estructura cinemática latente bajo una historia observada; el resultado negativo *Heart Sūtra*–TTC–Aristóteles impide convertir semejanzas verbales en genealogía.


# 2. Índice cronológico

Fechas antiguas aproximadas. Cuando la doctrina sobrevive en un testimonio posterior se separa fecha del argumento y del testigo. «Ingestión»: prioridad S4 para H10 (A/B/C) · asignación S5 (H10 estático / H11 dinámico). Las dos definiciones de H10/H11 difieren (§7.1, D13). Ejes según la tabla temática de S4; con asterisco, asignación derivada de S5.

| Nº | Fecha | Fuente · locus | Estado | Eje | Ingestión |
|:--|:------|:------------------|:-----------|:--|:----|
| E01 | s. V a. C.; testigo s. VI d. C. | Zenón vía Simplicio, *In Phys.* 139.7–15, 141.1 ss. (DK B1) | Confirmado (transmisión doxográfica) | C | — |
| E02 | s. IV–III a. C. (S4) / VI–V a. C. (S5) | Laozi, *Dao De Jing* 14 | Texto confirmado; vínculo atomista no sustentado | — | apéndice (S5) |
| E03 | s. IV a. C. | Aristóteles, *Physics* VI.1, 231a21–231b18 | Confirmado | C | A · H10 |
| E04 | s. IV a. C. | Aristóteles sobre Leucipo/Demócrito: *GC* I.8–9 (≈325a); *Metaph.* I.4 | Confirmado; corrección terminológica | P | — · H10 |
| E05 | s. IV–III a. C. | *Mohist Canon* A2, A61, A69 (red A52–A69) | Confirmado | C, B | A · H10 |
| E06 | s. IV–III a. C. | *Mohist Canon* B17 (sombra) | Confirmado | R* | — · H11 |
| E07 | 2022 | Schemmel & Boltz, *Theoretical Knowledge in the Mohist Canon* | Confirmado; fecha 2022 | — | — |
| E08 | 1965–2006 | Bibliografía mohista: Graham 1978, 1981; Graham & Sivin 1973; Boltz 2006; Yang Bojun 1965; Dai Nianzu 2001b | Confirmado (S1) | — | — |
| E09 | s. III a. C. | Arquímedes, *Method* prop. 2 | Contenido confirmado; pin crítico pendiente | S | — · H11 |
| E10 | c. 300 a. C. | Epicuro, *Carta a Heródoto* §§56–59 | Confirmado | C, B | — · H10 |
| E11 | s. III–II a. C. | *Zhuangzi* 33 «Tianxia» | Confirmado | M | — |
| E12 | incierta (peripatético antiguo) | Ps.-Aristóteles, *Mechanica* 24 | Confirmado; pseudoaristotélico | M | — |
| E13 | — | Ps.-Aristóteles, *De lineis insecabilibus* | Mencionado; sin pin | — | — |
| E14 | c. s. II a. C.–II d. C. | *Nyāya Sūtra* 4.2.23–25 | Confirmado | C | A · H10 |
| E15 | — | Nyāya: compuesto perceptible (*avayavin*), NS 2.1.35–36 | Vía IEP (secundaria) | B | — |
| E16 | — | Vaiśeṣika: origen de la magnitud perceptible | Vía SEP (secundaria) | — | — |
| E17 | s. I a. C.–I d. C.; com. 263 | *Nine Chapters* + Liu Hui: datación y autoría | Confirmado con distinción autoral | — | — |
| E18 | c. 150–250 | Nāgārjuna, *MMK* II.1–25 | Confirmado | M | — · H11 |
| E19 | 263 | Liu Hui, corte del círculo | Confirmado | S | A · H11 |
| E20 | 263 | Liu Hui, disección *yangma/bienao* (*Shanggong*) | Confirmado; nota previa mislocated | S | A · H11 |
| E21 | c. s. II–V (S4) / I–V (S5) | *Tattvārthasūtra* 5.6, 5.11, 5.14, 5.17, 5.32/33 + Pūjyapāda | Confirmado; numeración variable | B | A · H10 |
| E22 | c. s. III–IV | *Tathāgatagarbha Sūtra* | Confirmado; sin vínculo atomista | — | — |
| E23 | s. IV–V | Vasubandhu, *Abhidharmakośabhāṣya* I ad 43d | Contenido confirmado; edición pendiente | C | — |
| E24 | s. IV–V (S4) / V (S5) | Vasubandhu, *Viṃśatikā* 11–13/15, v. 12 | Confirmado directamente | C | A · H10 |
| E25 | s. V | Proclo, *In Eucl.* Def. II | Confirmado; pin Friedlein pendiente | M, G | — · H11 |
| E26 | s. V–VI | Zu Geng(zhi), principio de secciones | Confirmado como tradición textual | S | — · H11 |
| E27 | c. 480–540 (S4) / s. V (S5) | Dignāga, *Ālambanaparīkṣā* 1–2 | Confirmado; edición crítica pendiente | R | — · H10; H11 (S4) |
| E28 | s. VII | *Heart Sūtra*, 84000 Toh 531 §§1.6–1.11; T251 | Texto confirmado; eco atomista no sustentado | R | B · apéndice |
| E29 | s. VII | Woncheuk, comentario al *Heart Sūtra* | Parcial | — | C |
| E30 | m. c. 835; testigo s. XI–XII | al-Naẓẓām, *ṭafra*, vía al-Shahrastānī | Confirmado indirectamente; cautela Haarbrücker | M | — |
| E31 | 826–901 | Thābit ibn Qurra, *Ṣifat al-wazn*; *Qarasṭūn* | Confirmado (S4); `UNSPECIFIED` (S5) | S | A |
| E32 | s. X–XI | al-Qūhī y al-Sijzī, «compás perfecto» | Parcial | G | — |
| E33 | 980–1037 | Ibn Sīnā, *Physics* III.4, 189.14–190.3 (contacto) | Confirmado directamente | C* | A · H10 |
| E34 | 980–1037 | Ibn Sīnā, *Physics* III.3.15–16; III.4 §12 (piedra de molino) | Confirmado | M* | A · H11 |
| E35 | 2010 | McGinnis, *Avicenna* (OUP) | Confirmado | — | — |
| E36 | 2009 | Avicenna, *The Physics of The Healing*, ed. McGinnis (BYU) | Confirmado bibliográficamente | — | — |
| E37 | c. 1070 (vida 1048–1131) | ʿUmar Khayyām, tratado sobre los postulados de Euclides | Argumento confirmado; pin árabe parcial | G | — |
| E38 | s. XII (1077–1152) | Abū al-Barakāt al-Baghdādī, *Kitāb al-Muʿtabar* | Parcial | — | — |
| E39 | c. 1150 | Bhāskara II, *Siddhāntaśiromaṇi* | Parcial | — | — |
| E40 | c. 1190 (vida 1138–1204) | Maimónides, *Guía* I.73 | Confirmado; testimonio crítico externo | — | — · H11 |
| E41 | c. 1200 | Fakhr al-Dīn al-Rāzī, *al-Maṭālib al-ʿāliya* VI 48–49, 52, 71 | Confirmado | M, G | A · H11 |
| E42 | c. 1260–1270 | Aquinas, *SCG* III.64–77 | Mislocated temáticamente | — | — |
| E43 | c. 1260s (vida 1201–1274) | Ṭūsī, *al-Tadhkira* II.11 | Confirmado con pin | M, G | A · H11 |
| E44 | c. 1300 | Duns Scotus, *Ordinatio* II d.2 p.2 q.5 nn. 284–376 | Confirmado; corrección Vives | C | B · H10 |
| E45 | c. 1310s (vida c. 1270–1317) | Henry of Harclay, *Quaestiones ordinariae* | Confirmado doctrinalmente; pin pendiente | — | — · H10 |
| E46 | c. 1320s–1330s (vida 1290–1343) | Walter Chatton | Parcial | — | — · H10 |
| E47 | c. 1330s (vida c. 1298–1358) | Adam Wodeham, *Tractatus de indivisibilibus* | Confirmado | C | B |
| E48 | c. 1335 (vida c. 1313–1372) | William Heytesbury, *Regulae solvendi sophismata* IV–VI | Confirmado en estructura; folio pendiente | R | — · H11 |
| E49 | 1635 | Cavalieri, *Geometria indivisibilibus* | Confirmado; edición digital pendiente | S | — · H11 |
| E50 | 1638 | Galileo, *Discorsi*, Prima giornata | Confirmado; facsímil pendiente | M | — |
| E51 | c. 1700 | Choe Seok-jeong, *Gusuryak* 九數略 | Auténtico; ajuste temático débil | — | fuera de H10 |
| E52 | vida 1684–? | Hong Jeong-ha (solo S5) | Analogía lateral | — | — |
| E53 | 1722 | Takebe Katahiro, *Tetsujutsu Sankei* | Parcial (edición) | S | — · H11 |
| E54 | c. 1760s–1770s | Hong Dae-yong, *Ŭisan mundap* 醫山問答 | Confirmado (obra/doctrina); pin pendiente | R | B |
| E55 | 1836 | Choe Han-gi, *Gicheukcheui* / *Ch'uch'ŭkrok* (推動測靜) | Bibliografía confirmada; pasaje parcial | R | C · H11 |
| E56 | 1857–1867 | Choe Han-gi, *Kihak*; *Unhwa ch'ŭkhŏm*; *Sŏnggi unhwa* | Confirmado bibliográficamente | — | — |
| E57 | 1967/1968 | Kochen & Specker, *J. Math. Mech.* 17 | Confirmado; dos fechas | R | H11 (S4) |
| E58 | sin fecha en fuentes | *Ratnagotravibhāga* I.154–155 / I.157–158 | Confirmado (pasaje) | P | B |
| E59 | sin fecha en fuentes | *Śrīmālādevīsiṃhanāda* | Citado como autoridad por el RGV | P | — |


# 3. Fichas por entrada

Campos: fecha y lengua · locus/texto · contenido · edición y URL · estado · relevancia según las pasadas · notas · procedencia. Los URL se dan sin el parámetro `utm_source=chatgpt.com` que añadían las exportaciones.

### E01 · Zenón de Elea, fragmentos conservados por Simplicio

::: ficha
| | |
|:--|:-------------|
| Fecha · lengua | Argumento s. V a. C.; testigo Simplicio, s. VI d. C. · griego |
| Locus | Simplicio, *In Phys.* 139.7–15; 141.1 ss. (S4). *In Phys.* 139.9 y 141.2, DK B1 (S2). |
| Contenido | Si algo sin magnitud se añade a otra cosa y no la hace mayor, lo añadido es nada. Si cada existente tiene magnitud, siempre hay otra parte delante y la división no termina. El testigo es Simplicio, no un manuscrito de Zenón. |
| Edición | H. Diels, *Simplicii in Aristotelis Physicorum libros commentaria*, CAG IX, Berlín, 1882. La SEP localiza y analiza estos fragmentos. |
| URL | <https://seop.illc.uva.nl/entries/zeno-elea/> (S4) · <https://seop.illc.uva.nl//archives/fall2015/entries/paradox-zeno/> (S2) |
| Estado | Confirmado, con la cautela de transmisión doxográfica (S4). |
| Relevancia | Problema de la magnitud en forma directa: cómo una propiedad extensiva del conjunto surge de constituyentes que aportan cero; S2 lo valora como más cercano a la pregunta del programa que las paradojas del movimiento [cortado]. |
| Procedencia | S2, S4, S5 |
:::

### E02 · Laozi, *Dao De Jing* (*Tao Te Ching*) 14

::: ficha
| | |
|:--|:-------------|
| Fecha · lengua | s. IV–III a. C. (S4); c. s. VI–V a. C. (S5) (D01) · chino clásico |
| Texto | `視之不見` mirándolo, no se ve · `聽之不聞` escuchándolo, no se oye · `搏之不得` intentando asirlo, no se obtiene · `故混而為一` los tres se mezclan/unifican · `無狀之狀，無物之象` forma de lo sin forma, imagen de lo que no es cosa. |
| Contenido | Sujeto del capítulo: el Dao. Prosigue con lo innombrable, la imposibilidad de ver su frente o espalda y el gobierno de lo presente mediante el Dao antiguo. Las versiones de seda de Mawangdui (A/B) conservan el núcleo con diferencias de orden y grafía. Vocabulario de `微` «sutil/fino» (tabla §4.2). |
| URL | Texto recibido: <https://www.tao-te-ching.org/14> · Variantes Mawangdui A/B: <https://daodejing.ru/fr/chapters/14> |
| Estado | Texto confirmado; supuesto vínculo atomista no sustentado (S4). S5: no tratar como teoría corpuscular ni evidencia de atomismo. |
| Relevancia | Comparación tipológica con una realidad no accesible a los sentidos ordinarios (S4); lectura epistémica: lo que está en juego no se estabiliza como objeto sensorial ordinario (S5). Vínculo con el pasaje de los sentidos del *Heart Sūtra*: §4. |
| Procedencia | S4, S5 |
:::

### E03 · Aristóteles, *Physics* VI.1, 231a21–231b18

::: ficha
| | |
|:--|:-------------|
| Fecha · lengua | s. IV a. C. · griego |
| Contenido | Define continuo, contacto y sucesión. Una línea continua no puede componerse de puntos indivisibles: un indivisible no tiene extremos distintos que puedan coincidir o tocarse como exige la continuidad. Dos puntos sin partes no pueden ser continuos ni estar propiamente «en contacto»; si se tocan todo-con-todo (*whole-to-whole*) no producen continuidad. Extiende el argumento conjuntamente a magnitud, tiempo y movimiento: sus estructuras deben ser compatibles. |
| Edición | Números Bekker; texto/trad. Hardie–Gaye (S4). S4 pide para H10 texto griego crítico + Bekker + traducción moderna. |
| URL | <https://www.logoslibrary.org/aristotle/physics/601.html> (S4) · <https://www.logicmuseum.com/wiki/Authors/Aristotle/physics/liber6> (S2) · <https://classics.mit.edu/Aristotle/physics.6.vi.html> (S5) |
| Estado | Confirmado. Prioridad H10 máxima (S4). |
| Relevancia | Formulación abstracta del problema; contrapunto a Vasubandhu. No pregunta solo por la divisibilidad infinita: pregunta qué relación de contacto convertiría simples en un continuo (S2). Espejo: Maimónides I.73 (E40). |
| Procedencia | S2, S4, S5 |
:::

### E04 · Aristóteles como informante del atomismo de Leucipo y Demócrito

::: ficha
| | |
|:--|:-------------|
| Fecha · lengua | s. IV a. C. · griego |
| Locus | *De generatione et corruptione* (*Generation and Corruption*) I.8–9, especialmente ≈325a ss. (S4). *Metaphysics* I.4 (S5). Loci complementarios (D02). |
| Contenido | Cuerpos indivisibles, innumerables en figura; los compuestos difieren por figura, orden/agrupación y posición. Es exposición del atomismo democriteo para criticarlo, no doctrina aristotélica. |
| Edición | Texto griego, ed. Bekker 1831 (catálogo Perseus); trad. Joachim (MIT Classics); trad. inglesa en ellopos; *Metaphysics* trad. Ross 1908 (Wikisource). |
| URL | <https://catalog.perseus.org/catalog/urn:cts:greekLit:tlg0086.tlg013.opp-grc1> · <https://classics.mit.edu/Aristotle/gener_corr.html> · <https://www.ellopos.net/elpenor/greek-texts/ancient-greece/aristotle/generation-corruption.asp> · <https://en.wikisource.org/wiki/Page:Metaphysics_by_Aristotle_Ross_1908_(deannotated).djvu/31> |
| Estado | Confirmado; corrección terminológica. |
| Nota | Evitar «átomos aristotélicos» / «Aristotelian atom properties». Usar «Democritean atomism as reported and criticized by Aristotle». Mantener separado del rechazo aristotélico del continuo compuesto de indivisibles (E03). |
| Procedencia | S4, S5 |
:::

### E05 · *Mohist Canon* A2, A61, A69 (extremo, parte, contigüidad)

::: ficha
| | |
|:--|:-------------|
| Fecha · lengua | s. IV–III a. C. · chino clásico |
| Texto | A61 define `端` *duān*, extremo (*endpoint*), como `體之無厚而最前者也`: elemento sin grosor/magnitud situado en el extremo. |
| Contenido | A69: lo contiguo es estar sin intervalo y sin solaparse; la explicación dice que es posible porque el extremo carece de magnitud. A2 define `體` *tǐ* como parte/elemento de un todo compuesto, con el extremo de una vara de medir como ejemplo. Schemmel–Boltz muestran que el vocabulario geométrico forma una red sistemática A52–A69: *part*, *whole*, *overlap*, *gap*, *contiguous* pertenecen al mismo sistema, no son definiciones aisladas. |
| Edición | Schemmel & Boltz 2022, cap. «Text and Translation» (E07). |
| URL | <https://link.springer.com/chapter/10.1007/978-3-031-08797-4_2> (cap. «The Mohist Canon and Alternative Origins of Theoretical Science»; S2, S4) · <https://www.mprl-series.mpg.de/studies/8/5/index.html> (S2) · <https://link.springer.com/book/10.1007/978-3-031-08797-4> |
| Estado | Confirmado. Guardar A61/A69 aparte de B17 (S4). |
| Relevancia | Propuesta positiva de una teoría rudimentaria del contacto: dos extensiones son contiguas gracias a un límite no extenso (S2). Límite sin extensión ≠ constituyente; contigüidad positiva (S4). Uso protopológico positivo de fronteras no extensas (S5). S2 lo cuenta entre los mejores hallazgos nuevos y pide nota propia distinta de B17. |
| Procedencia | S2, S4, S5 |
:::

### E06 · *Mohist Canon* B17 — «la sombra no se desplaza»

::: ficha
| | |
|:--|:-------------|
| Fecha · lengua | s. IV–III a. C. · chino clásico |
| Texto | `景不徙。說在改為。` Trad. Schemmel–Boltz: «A shadow does not shift about. The explanation lies with being re-cast.» (S1). S5-EN: «…being re-formed»; S5-ES: «…ser rehecha/reformada» (D14). |
| Contenido | La explicación añade que al llegar la luz desaparece la sombra anterior; el comentario interpreta la aparente traslación como extinción y nueva formación en otro lugar. |
| Paralelos | *Liezi*: `影不移者說在改也` (Yang Bojun 1965, p. 88, citado por Schemmel–Boltz p. 132); transmite una forma posterior del motivo de B17 (S1). Pasajes ópticos B17–B2[…] en Graham & Sivin 1973; B18/B19 en Dai Nianzu 2001b (E08). |
| URL | <https://upload.wikimedia.org/wikipedia/commons/6/6f/Matthias_Schemel_and_William_G._Boltz_-_Theoretical_Knowledge_in_the_Mohist_Canon.pdf> (S1) |
| Estado | Confirmado directamente (S1); S1 añade una observación sobre la conexión con la óptica [cortado]. |
| Relevancia | Óptica y persistencia de un efecto observado (S4). Continuidad fenomenológica sin transporte material de una entidad persistente (S5). Con Dignāga: causa del registro ≠ objeto representado (S5 §1.4). No confundir con la sombra del ave del *Zhuangzi* (E11). |
| Procedencia | S1, S4, S5 |
:::

### E07 · Schemmel & Boltz, *Theoretical Knowledge in the Mohist Canon* (edición de referencia)

::: ficha
| | |
|:--|:-------------|
| Datos | Matthias Schemmel & William G. Boltz, *Theoretical Knowledge in the Mohist Canon*, Archimedes 63, Springer. DOI 10.1007/978-3-031-08797-4. © 2022; softcover 30-12-2022; eBook 01-01-2023; hardcover 02-01-2023. |
| URL | <https://link.springer.com/book/10.1007/978-3-031-08797-4> · <https://doi.org/10.1007/978-3-031-08797-4> · PDF: <https://upload.wikimedia.org/wikipedia/commons/6/6f/Matthias_Schemel_and_William_G._Boltz_-_Theoretical_Knowledge_in_the_Mohist_Canon.pdf> (el nombre de archivo del URL escribe «Schemel») |
| Estado | Confirmado, con corrección de fecha (S1). |
| Corrección | El archivo local `SchemmelBoltz_MohistCanon_2023.pdf` es comprensible por la fecha del eBook, pero la cita bibliográfica debe ser **Schemmel & Boltz 2022**; anotar «electronic publication 2023» solo si el sistema necesita fecha de versión digital (S1, S4). |
| Uso | Edición integrada para A2/A61/A69 y B17. Contiene la bibliografía de E08. |
| Procedencia | S1, S4 |
:::

### E08 · Bibliografía mohista y *Zhuangzi* verificada en S1

::: ficha
| | |
|:--|:-------------|
| Graham 1978 | A. C. Graham, *Later Mohist Logic, Ethics, and Science*, Hong Kong/London: Chinese University Press / SOAS, 1978. Fuente fundamental de Schemmel–Boltz; es el «Graham» que aparece en la salida del transcript. |
| Graham 1981 | A. C. Graham, *Chuang-tzŭ: The Inner Chapters*, London: George Allen & Unwin, 1981. Schemmel–Boltz lo usan para las traducciones de las líneas paradójicas vecinas a la de la sombra. |
| Graham & Sivin 1973 | A. C. Graham & Nathan Sivin, «A Systematic Approach to the Mohist Optics (ca. 300 B.C.)», en *Chinese Science: Explorations of an Ancient Tradition*, eds. Needham, Nakayama & Sivin, MIT Press, 1973, pp. 105–152. Referencia histórica para interpretar los pasajes ópticos B17–B2[…]. |
| Boltz 2006 | William G. Boltz, «Mechanics in the ‘Mohist Canon’: Preliminary Textual Questions», en *Studies on Ancient Chinese Scientific and Technical Texts: Proceedings of the 3rd ISACBRST*, Zhengzhou: Daxiang chubanshe, 2006, pp. 32–40. Es el «Boltz» que aparece aislado en la salida del transcript. |
| Yang Bojun 1965 | Yang Bojun 楊柏峻, *Liezi jishi* 列子集釋, Hong Kong: Taiping shuju, 1965. Schemmel–Boltz p. 132 remiten a p. 88 para el paralelo `影不移者說在改也`. |
| Dai Nianzu 2001b | Dai Nianzu 戴念祖, *Guangxue shi* 光学史 [historia de la óptica], Changsha: Hunan jiaoyu chubanshe, 2001. En Schemmel–Boltz, discusión de B18/B19. |
| URL | Todas localizadas en la bibliografía de Schemmel–Boltz: PDF de Wikimedia (E07). |
| Estado | Confirmado (las seis). |
| Procedencia | S1 |
:::

### E09 · Arquímedes, *Method*, prop. 2

::: ficha
| | |
|:--|:-------------|
| Fecha · lengua | s. III a. C. · griego |
| Contenido | Corta esfera, cono y cilindro por planos paralelos, trata cada sección como peso y demuestra el equilibrio sección por sección mediante la ley de la palanca; después pasa al equilibrio de los sólidos completos. La estructura local de todas las secciones permite inferir la relación global de volúmenes. |
| Edición | Proposición reconstruida en ediciones modernas del *Method*; para H10, edición Heiberg/Heath o Netz antes que una página divulgativa (S4). |
| URL | <https://old.maa.org/press/periodicals/convergence/archimedes-method-for-computing-areas-and-volumes-proposition-2-of-the-method?device=mobile> (S2) · <https://old.maa.org/> (S5, genérico) |
| Estado | Contenido confirmado; pin crítico no rehecho (S4). Confirmado (S2). |
| Relevancia | «Statics before dynamics»: sin preguntar de qué está hecho el sólido, una familia de restricciones estáticas locales (secciones) determina una propiedad global; forma antigua de reconstrucción desde datos locales (S2, parcialmente cortado). |
| Procedencia | S2, S4, S5 |
:::

### E10 · Epicuro, *Carta a Heródoto* (*Letter to Herodotus*) §§56–59

::: ficha
| | |
|:--|:-------------|
| Fecha · lengua | c. 300 a. C. (S4); s. III a. C. (S5) (D06) · griego |
| Contenido | Rechaza la divisibilidad física indefinida. El átomo tiene tamaño; dentro de él hay *minima* conceptuales que sirven como unidades/límites de medida pero no se agregan ni se mueven como cuerpos pequeños independientes. §§58–59 distinguen mínimo perceptible, mínimo conceptual y átomo. |
| Edición | Cyril Bailey, *Epicurus: The Extant Remains*, 1926 (texto griego/inglés). |
| URL | <https://ericlyonshansen.github.io/Epicurus/Letter_to_Herodotus_Bailey.html> (S4) · <https://ericlyonshansen.github.io/Epicurus/Letter_to_Herodotus_Bailey_Lines.html> (S2) · <https://societyofepicurus.com/epicurus-epistle-to-herodotus/> (S4, nota 11) |
| Estado | Confirmado. |
| Relevancia | Tercera opción entre «punto sin extensión» y «continuo infinitamente divisible»: el átomo es extenso, los mínimos son estructura geométrica, no constituyentes independientes (S2, S4, S5). |
| Procedencia | S2, S4, S5 |
:::

### E11 · *Zhuangzi* 33, «Tianxia» 天下

::: ficha
| | |
|:--|:-------------|
| Fecha · lengua | s. III–II a. C. (S4); s. III a. C. (S5) · chino clásico |
| Texto | En el mismo párrafo: `飛鳥之景未嘗動也` (la sombra del ave en vuelo nunca se ha movido); `鏃矢之疾而有不行不止之時` (la flecha rápida tiene un momento en que ni avanza ni está detenida); `一尺之捶，日取其半，萬世不竭` (de una vara de un pie se quita la mitad cada día y no se agota en diez mil generaciones). |
| Contexto | Enunciados preservados en el *Zhuangzi* dentro de una lista asociada a los *bian*[zhe] (S1, cortado). |
| URL | <https://zh.wikisource.org/wiki/%E8%8E%8A%E5%AD%90/%E5%A4%A9%E4%B8%8B> (S1) · <https://zh.wikisource.org/zh-hant/莊子/天下> (S4) |
| Estado | Confirmado directamente (S1, S4). |
| Nota | No identificar automáticamente la sombra del ave con B17 del *Mohist Canon* (S1, S4, S5). |
| Procedencia | S1, S4, S5 |
:::

### E12 · Pseudo-Aristóteles, *Mechanica* 24 (rueda)

::: ficha
| | |
|:--|:-------------|
| Fecha · lengua | Incierta, período peripatético antiguo · griego |
| Contenido | Dos círculos concéntricos rígidamente unidos completan una revolución con el mismo desplazamiento lineal aunque sus circunferencias difieren. El texto observa que el círculo mayor no se detiene y el menor no salta ningún punto, y aun así recorren «la misma» distancia. Fuente de la posterior «rueda de Aristóteles». Atribución no auténtica. |
| URL | <https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Aristotle/Mechanica%2A.html> |
| Estado | Confirmado, pero pseudoaristotélico. |
| Relevancia | Paradoja sobre qué puntos de una configuración rígida «cuentan» como longitud; conduce a Galileo (E50). Genealogía propuesta en S2: *Mechanica* → Galileo → indivisibles. |
| Procedencia | S2, S4 |
:::

### E13 · Pseudo-Aristóteles, *De lineis insecabilibus* (*Sobre las líneas indivisibles*)

::: ficha
| | |
|:--|:-------------|
| Mención | En el mapa de candidatos recordados de S4. Texto cuya problemática reutiliza Harclay (E45) y cuya recepción latina es pieza central de Wodeham (E47); estudio: Crialesi, REFIME (E45). |
| Estado | Sin pin ni edición en las fuentes. |
| Procedencia | S4 |
:::

### E14 · *Nyāya Sūtra* 4.2.23–25 (partes del átomo)

::: ficha
| | |
|:--|:-------------|
| Fecha · lengua | c. s. II a. C.–II d. C. · sánscrito |
| Contenido | 4.2.23: objeción, el átomo debe tener partes porque tiene forma/configuración. 4.2.24: porque puede entrar en conjunción con otro átomo. 4.2.25: respuesta, admitir partes conduce a *anavasthā*, regresión infinita. |
| URL | Texto electrónico, Univ. de Delhi: <https://cl.sanskrit.du.ac.in/etexts/etext.php?text=nyayasutra> |
| Estado | Confirmado. Contrapunto a Vasubandhu (S4). |
| Relevancia | El mismo dilema que Vasubandhu/Aristóteles, con respuesta realista atomista (S2, S4). |
| Procedencia | S2, S4, S5 |
:::

### E15 · Nyāya: el compuesto perceptible (*avayavin*)

::: ficha
| | |
|:--|:-------------|
| Locus | *Nyāya Sūtra* 2.1.35–36 según la IEP, con el argumento epistemológico asociado. |
| Contenido | El compuesto no se reduce al agregado de partes, entre otras razones porque vemos el objeto compuesto y no sus átomos. |
| URL | <https://iep.utm.edu/nyaya/> |
| Estado | Localizado vía fuente secundaria (IEP). |
| Relevancia | Desplaza la pregunta de «cómo se forma la extensión» a qué es el objeto del registro perceptivo (S2, cortado). Microconstituyentes no idénticos al objeto macroscópico de percepción (S5). Eje B en S4. |
| Procedencia | S2, S4, S5 |
:::

### E16 · Vaiśeṣika: origen de la magnitud perceptible

::: ficha
| | |
|:--|:-------------|
| Contenido | Si átomo y díada son imperceptiblemente pequeños, ¿por qué la tríada tiene magnitud perceptible? Se rechaza que sea magnitud heredada de los componentes o producida por huecos entre ellos; la explicación estándar hace surgir la magnitud macroscópica de la pluralidad/número de componentes. |
| URL | <https://plato.stanford.edu/entries/naturalism-india/> |
| Estado | Localizado vía SEP; sin pin primario. |
| Relevancia | Teoría de emergencia de una propiedad geométrica que no se obtiene sumando la misma propiedad microscópica (S3, cortado). |
| Procedencia | S3 |
:::

### E17 · *Nine Chapters* / *Jiǔzhāng suànshù* y comentario de Liu Hui: datación y autoría

::: ficha
| | |
|:--|:-------------|
| Fecha · lengua | Compilación s. I a. C.–I d. C.; comentario de Liu Hui, 263 · chino clásico |
| Contenido | Los pasajes de límite relevantes son sobre todo del comentario de Liu Hui; no atribuirlos sin más al texto Han. |
| URL | <https://en.wikipedia.org/wiki/The_Nine_Chapters_on_the_Mathematical_Art> · <https://liucan.me/projects/chinese-calculus/> |
| Estado | Confirmado con distinción autoral. |
| Procedencia | S4 |
:::

### E18 · Nāgārjuna, *Mūlamadhyamakakārikā* II

::: ficha
| | |
|:--|:-------------|
| Fecha · lengua | c. 150–250 (S4); c. s. II–III (S5) (D07) · sánscrito |
| Texto | MMK 2.1: `gataṃ na gamyate … agataṃ … gamyamānaṃ na gamyate`. |
| Contenido | Lo ya recorrido no está siendo recorrido; tampoco lo no recorrido; y se problematiza el supuesto «presente recorrido» intermedio. El capítulo (II.1–25) desmantela la localización del movimiento en móvil, trayecto e instante. |
| URL | GRETIL, enlace usado en el transcript: <https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/6_sastra/3_phil/buddh/nagmmk_u.htm> (S1) · GRETIL TEI: <https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/html/sa_nAgArjuna-mUlamadhyamakakArikA.htm> (S4) |
| Estado | Confirmado directamente. |
| Nota | Nāgārjuna problematiza/niega que el movimiento pueda localizarse en las tres alternativas; no hace una clasificación neutral de tres clases de trayectoria (S1, S4). |
| Relevancia | Una trayectoria no se descompone ingenuamente en estados estáticos independientes (S5). |
| Procedencia | S1, S4, S5 |
:::

### E19 · Liu Hui, corte del círculo (263)

::: ficha
| | |
|:--|:-------------|
| Locus | Comentario a «`半周半徑相乘得積步`» (*Nine Chapters*, juan 1). |
| Texto | `割之彌細，所失彌少。割之又割，以至於不可割…` (forma larga en S5; S1/S4: `割之彌細，所失彌少。割之又割…`). |
| Contenido | Cuanto más fina la división, menor la pérdida; se continúa hasta que el polígono coincide con el círculo sin pérdida. |
| Edición | Facsímil chino + edición crítica (S4). |
| URL | <https://zh.wikisource.org/zh-hant/劉徽割圓術> (S1, S4) · <https://liucan.me/projects/chinese-calculus/> (S4; reconstrucción textual que conserva la fórmula del círculo y la de Zu Geng) |
| Estado | Confirmado como referencia distinta de la disección sólida. |
| Relevancia | Refinamiento y pérdida; reconstrucción global por refinamiento iterativo (S4, S5). |
| Nota | El archivo local `NineChapters_juan1_LiuHui_circle_cutting…` no sustenta la afirmación «shrinking remainder in solid dissection» (→ E20; corrección §6, nº 1). |
| Procedencia | S1, S4, S5 |
:::

### E20 · Liu Hui, disección *yangma* / *bienao* (sección *Shanggong* 商功)

::: ficha
| | |
|:--|:-------------|
| Locus | *Nine Chapters*, sección `商功` *Shanggong*, problema del `陽馬` *yangma*; páginas facsimilares 18–19 de la edición Sibu Congkan. |
| Contenido | p. 18: descomposición en `鼈臑` (*bienao*) y `陽馬` (*yangma*). p. 19: al volver a reducir a la mitad, el resto se hace cada vez menor y fino hasta `微`, «sin forma»; se pregunta dónde quedaría resto alguno. |
| URL | p. 18: <https://zh.wikisource.org/wiki/Page%3ASibu_Congkan0391-%E5%8A%89%E5%BE%BD-%E4%B9%9D%E7%AB%A0%E7%AE%97%E8%A1%93-3-2.djvu/18> · p. 19 (pasaje límite): <https://zh.wikisource.org/wiki/Page%3ASibu_Congkan0391-%E5%8A%89%E5%BE%BD-%E4%B9%9D%E7%AB%A0%E7%AE%97%E8%A1%93-3-2.djvu/19> |
| Estado | Confirmado; el transcript mezclaba dos argumentos distintos de Liu Hui. Este es el de la disección sólida, no el comentario del círculo (S1). Nota previa del repositorio parcialmente mislocated (S4). |
| Nota | El transcript buscó la página /18 y después formuló la conclusión sobre la disección sólida (S1). Crear nota separada (§6, nº 1; §7.2). |
| Procedencia | S1, S4, S5 |
:::


### E21 · Umāsvāti/Umāsvāmin, *Tattvārthasūtra*, con el comentario de Pūjyapāda (*Sarvārthasiddhi*)

::: ficha
| | |
|:--|:-------------|
| Fecha · lengua | c. s. II–V (S4); c. s. I–V d. C. (S5) (D08) · sánscrito |
| 5.6 | *Dharma*, *adharma* y espacio son cada uno un solo *dravya*, aunque espacialmente tengan innumerables regiones. |
| 5.11 | El *paramāṇu* no tiene partes espaciales internas (subdivisiones como un cuerpo ordinario) y corresponde a un *pradeśa*. |
| 5.14 | Comentario: dos o más partículas pueden ocupar un único *pradeśa*, incluso sin estar combinadas; analogía de luces que se interpenetran. |
| 5.17 | *Dharma* y *adharma* son medios que asisten movimiento y reposo; no empujan ni frenan activamente. |
| 5.32/5.33 | `snigdharūkṣatvād bandhaḥ`: *snigdha*/*rūkṣa* como condición de *bandha*. Pūjyapāda pregunta si basta la mera unión y responde que no: determinadas transformaciones/cualidades permiten que varios átomos se conviertan en un solo *skandha*. La tradición comentarial añade reglas por grados. Numeración 5.32 o 5.33 según recensión. |
| URL | Sitio *Tattvārtha Sūtra with Commentary* (wisdomlib). 5.11: <https://www.wisdomlib.org/jainism/book/tattvartha-sutra-with-commentary/d/doc1084765.html> · 5.14: <https://www.wisdomlib.org/jainism/book/tattvartha-sutra-with-commentary/d/doc1084768.html> · 5.33: <https://www.wisdomlib.org/jainism/book/tattvartha-sutra-with-commentary/d/doc1084787.html> · fila 5.6/5.17 de S3: <https://www.wisdomlib.org/jainism/book/tattvartha-sutra-with-commentary/d/doc1084760.html> (por la numeración correlativa de la serie corresponde a 5.6; inferencia, no verificada) |
| Estado | Confirmado, con variación 5.32/5.33. Guardar *incipit*, no solo número (S4). |
| Relevancia | Rompe número de constituyentes ≡ volumen ocupado; co-ubicación ≠ composición; *binding* como relación adicional; fondo cinemático sin fuerza (F6, F7). S3 lo propone como el hallazgo a desarrollar con más prioridad. |
| Procedencia | S3, S4, S5 |
:::

### E22 · *Tathāgatagarbha Sūtra*

::: ficha
| | |
|:--|:-------------|
| Fecha · lengua | c. s. III–IV · chino y tibetano; fragmentos sánscritos indirectos |
| Contenido | Nueve símiles (Buda dentro de loto marchito, miel entre abejas, grano bajo cáscara, oro oculto, tesoro enterrado, etc.) describen una naturaleza/capacidad búdica oculta por envolturas adventicias. No trata de partículas ni del continuo. |
| Testigos | Dos traducciones chinas (T666, T667), dos tibetanas (D258/Q924), citas sánscritas en el *Ratnagotravibhāga*. |
| Edición | Michael Zimmermann, *A Buddha Within*, 2002 (edición/estudio fundamental; rastrea qué formulaciones sobreviven como citas sánscritas en el RGV). |
| URL | <https://buddhanature.tsadra.org/index.php/Tath%C4%81gata_Essence_S%C5%ABtra> |
| Estado | Confirmado; vínculo con atomismo: no. |
| Procedencia | S4 |
:::

### E23 · Vasubandhu, *Abhidharmakośabhāṣya* I ad 43d

::: ficha
| | |
|:--|:-------------|
| Fecha · lengua | s. IV–V · sánscrito |
| Contenido | Pregunta literal: ¿los átomos se tocan o no? Los Kāśmīra: contacto total los mezclaría (colapso/interpenetración); contacto parcial les daría partes. Vasubandhu: los agregados no son otra cosa que los átomos agregados; discute qué significa estar sin intervalo. Inmediatamente después: cómo un órgano capta objetos mayores que él, y la analogía del círculo de fuego aparente. |
| URL | <https://wstb.univie.ac.at/wp-content/uploads/WSTB_94.pdf> (S2) |
| Estado | Contenido confirmado; edición primaria local pendiente: añadir texto sánscrito crítico del AKBh en vez de depender solo del PDF secundario (S4). |
| Relevancia | Une contacto microscópico → agregado macroscópico → percepción de extensión; puente entre estructura estática y *measurement* (S2, cortado). Prepara el problema composición–extensión de la *Viṃśatikā* (S4). |
| Procedencia | S2, S4, S5 |
:::

### E24 · Vasubandhu, *Viṃśatikā-vijñaptimātratāsiddhi*, vv. 11–13 (11–15), esp. v. 12

::: ficha
| | |
|:--|:-------------|
| Fecha · lengua | s. IV–V (S4); s. V (S5) · sánscrito |
| Texto | `ṣaṭkena yugapad yogāt paramāṇoḥ ṣaḍaṃśatā` |
| Contenido | El contacto simultáneo con seis átomos (seis direcciones) implica seis partes/aspectos en el central; si todos ocupan el mismo lugar, el agregado no supera el tamaño de un átomo. |
| Edición | GRETIL, basado en la edición de Sylvain Lévi, 1925, con correcciones de Hakuju Ui, 1953. |
| URL | <https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/html/sa_vasubandhu-viMzatikA-vijJaptimAtratAsiddhi.htm> (S1) · <https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/6_sastra/3_phil/buddh/vasvvmsu.htm> (S4) |
| Estado | Confirmado directamente; la paráfrasis del transcript es fiel (S1). Prioridad H10 máxima (S4). |
| Nota | Rango: vv. 11–13 (S1, S5), 11–15 (S4) (D03). |
| Procedencia | S1, S4, S5 |
:::

### E25 · Proclo, comentario a Euclides, Def. II

::: ficha
| | |
|:--|:-------------|
| Fecha · lengua | s. V · griego |
| Contenido | Registra la definición alternativa de la línea como «flujo de un punto», y distingue: eso describe su causa generativa, no su esencia; la esencia geométrica es magnitud extendida en una dirección. |
| Edición | G. Friedlein, *Procli Diadochi in primum Euclidis Elementorum librum commentarii*, Leipzig, 1873. Comparación moderna sobre la distinción causal/conceptual (Cambridge). |
| URL | <https://www.cambridge.org/core/books/conceptualising-concepts-in-greek-philosophy/concepts-in-greek-mathematics/DC34401AA94103E01D51253EACB2C92D> («Concepts in Greek Mathematics», cap. 13 de *Conceptualising Concepts in Greek Philosophy*) |
| Estado | Pasaje confirmado; el pin Friedlein debe anotarse desde el facsímil al ingerirlo (S4). |
| Relevancia | Separa constitución estática de procedimiento de generación: una línea no está ontológicamente hecha de las posiciones de un punto aunque pueda generarse por movimiento (S2, S5). |
| Procedencia | S2, S4, S5 |
:::

### E26 · Zu Geng / Zu Gengzhi 祖暅, principio de secciones

::: ficha
| | |
|:--|:-------------|
| Fecha · lengua | s. V–VI · chino clásico |
| Texto | `冪勢既同，則積不容異`: si las áreas de las secciones correspondientes (y su disposición en altura) coinciden, los volúmenes no pueden diferir. |
| Transmisión | Frase conservada por Li Chunfeng (S2), en la transmisión comentarial de *Nine Chapters* (S4). |
| Edición | Traducción y reconstrucción completa de la demostración de la esfera: Donald Wagner (S2). S4 recomienda sustituir la web auxiliar por facsímil o edición Chemla–Guo. |
| URL | <https://www.donwagner.dk/SPHERE/SPHERE.html> · <https://donwagner.dk/SPHERE/SPHERE.html> (S2, dos formas) · <https://liucan.me/projects/chinese-calculus/> (S4) |
| Estado | Confirmado como tradición textual. |
| Relevancia | Paralelo independiente de Arquímedes/Cavalieri: no requiere que el sólido esté compuesto de secciones; la igualdad de todas las «observaciones» seccionales basta para fijar la igualdad tridimensional (S2, cortado; S5). |
| Procedencia | S2, S4, S5 |
:::

### E27 · Dignāga, *Ālambanaparīkṣā* 1–2

::: ficha
| | |
|:--|:-------------|
| Fecha · lengua | c. 480–540 (S4); s. V (S5) (D05) · sánscrito reconstruido / tibetano |
| Contenido | Para ser objeto de percepción, algo debe (a) causar la cognición y (b) corresponder a cómo aparece en ella. Los átomos pueden satisfacer la causalidad sin aparecer como átomos; el agregado parece corresponder a la forma percibida, pero Dignāga niega que tenga la realidad causal requerida. |
| URL | <https://journals.ub.uni-heidelberg.de/index.php/jiabs/article/download/8988/2881/8782> (JIABS; S3) · <https://plato.stanford.edu/entries/yogacara/> (S3) |
| Estado | Doctrina y versos confirmados mediante literatura académica; el repositorio necesita una edición crítica estable (S4). |
| Relevancia | *source ≠ represented object*; causa del registro ≠ objeto representado (S3, S5). S3 lo señala como sorpresa conceptual de la pasada. En H11 (S4) como distinción dignaguiana. |
| Procedencia | S3, S4, S5 |
:::

### E28 · *Prajñāpāramitāhṛdaya* / *Heart Sūtra*

::: ficha
| | |
|:--|:-------------|
| Fecha · lengua | s. VII · sánscrito / chino / tibetano |
| Locus | 84000, Toh 531, §§1.6–1.11; chino T251. |
| Contenido (S4) | §1.6: equivalencia forma–vacuidad. §1.7: los fenómenos son vacíos, sin características, no nacidos, no cesados, no manchados/no libres de mancha, ni deficientes ni completos. Después recorre agregados, sentidos, elementos, originación dependiente y cuatro verdades. Objetivo: ausencia de naturaleza intrínseca en agregados/dharmas. |
| Texto chino (S5) | `色即是空，空即是色` → `不生不滅 … 不增不減` → `無眼耳鼻舌身意；無色聲香味觸法` («No eye, ear, nose, tongue, body, or mind; no form, sound, smell, taste, touch, or dharmas»). Orden de la secuencia según S5-EN. |
| Edición | 84000 (traducción desde el tibetano; señala variantes entre testigos sánscritos, chinos y tibetanos). Jan Nattier 1992 (JIABS), estudio de la historia textual (S5). |
| URL | <https://reader.84000.co/entity/passage/4d1896b2-dcf3-4b01-8cc6-8bd5e30c9d67> · <https://84000.co/translation/toh531.pdf> · <https://journals.ub.uni-heidelberg.de/index.php/jiabs/article/view/8800> · <https://en.wikipedia.org/wiki/Heart_Sutra> |
| Estado | Texto confirmado; «eco atomista aristotélico» no sustentado (S4). |
| Relevancia | Con el pasaje de los sentidos, la comparación con TTC 14 es sensorial y epistemológica: ambos niegan que la realidad en cuestión sea capturable por las modalidades ordinarias de objetivación (S5). No es física corpuscular. §4. |
| Procedencia | S4, S5 |
:::

### E29 · Woncheuk 圓測, comentario al *Heart Sūtra*

::: ficha
| | |
|:--|:-------------|
| Fecha · lengua | s. VII, Silla–Tang · chino budista |
| Contenido | Monje coreano de Silla activo en China. La historiografía textual del *Heart Sūtra* usa los comentarios tempranos de Kuiji y Woncheuk como evidencia china del texto. Entrada coreana al problema de cómo interpretar vacuidad y agregados. |
| URL | <https://en.wikipedia.org/wiki/Heart_Sutra> (discusión de la historia textual) |
| Estado | Parcial. Número Taishō y folio no verificados; no fijar pin hasta comprobar CBETA/SAT (S4). |
| Relevancia | Puente Corea ↔ epistemología/vacuidad más orgánico que una obra matemática coreana incluida por cobertura geográfica (S4). |
| Procedencia | S4 |
:::

### E30 · al-Naẓẓām, teoría de la *ṭafra* («salto»), vía al-Shahrastānī

::: ficha
| | |
|:--|:-------------|
| Fecha · lengua | al-Naẓẓām m. c. 835; testimonio de al-Shahrastānī, s. XI–XII · árabe, doxográfico |
| Contenido | La *ṭafra* intenta explicar el movimiento bajo división espacial infinita (S5). Ejemplos: la hormiga y la cuerda del pozo (S5); en la tradición, la rueda/piedra de molino: radios diferentes generan problemas para pasos espaciales mínimos uniformes (S4). Ejemplos antiatomistas (S1). |
| Fuentes | al-Shahrastānī, *al-Milal wa-l-niḥal*; testigo manuscrito árabe Princeton, Garrett 4045Y. Traducción alemana: Theodor Haarbrücker, *Abu-'l-Fath Muh'hammad asch-Schahrastâni's Religionspartheien und Philosophen-Schulen*, vol. I, Halle: Schwetschke, 1850. |
| URL | Haarbrücker: <https://www.deutsche-digitale-bibliothek.de/item/36IDSI3RR6PD2TOYCV6GYZLQF533HUK2> · <https://opendata.uni-halle.de/bitstream/1981185920/47211/2/407352872.pdf> |
| Estado | Doctrina confirmada indirectamente (S4). La bibliografía moderna confirma la teoría y sus ejemplos antiatomistas; una fuente filológica posterior que reproduce el ejemplo de la hormiga afirma que la traducción de Haarbrücker de ese pasaje es incorrecta (S1). |
| Nota | Haarbrücker sirve como testigo histórico/OCR, no como única autoridad para una traducción final. Añadir edición árabe y traducción académica posterior; conservar la naturaleza doxográfica de la atribución (§6, nº 6). |
| Procedencia | S1, S4, S5 |
:::

### E31 · Thābit ibn Qurra, *Kitāb fī ṣifat al-wazn* y *Kitāb fī l-qarasṭūn*

::: ficha
| | |
|:--|:-------------|
| Fecha · lengua | 826–901 · árabe |
| Contenido (S4) | *Ṣifat al-wazn*: condiciones bajo las cuales una balanza está en equilibrio y condiciones para que la medición sea correcta con pesos, brazos y medios iguales o desiguales; obra de cinco secciones, cuya última contiene una proposición equivalente al postulado inicial del posterior *Qarasṭūn*. *Qarasṭūn*: tratamiento sistemático de la romana (*steelyard*), mecánica del equilibrio con brazos desiguales. |
| Manuscrito | *Qarasṭūn*: British Library, India Office Islamic 461, ff. 198v–207r, copia de 1198, digitalizada por Qatar Digital Library. |
| Estudio | Mohammed Abattouy, «Greek Mechanics in Arabic Context: Thābit ibn Qurra, al-Isfizārī and the Arabic Traditions of Aristotelian and Euclidean Mechanics», *Science in Context* 14 (2001), 179–247, DOI 10.1017/S0269889701000084. |
| URL | <https://al-furqan.com/the-corpus-of-the-arabic-science-of-weights-9th-19th-centuries-codicology-textual-tradition-and-theoretical-scope/?ver=2.0.3> (estudio del corpus árabe de pesos) · <https://en.wikipedia.org/wiki/Th%C4%81bit_ibn_Qurra> |
| Estado | S4: Confirmado; objetivo de alta prioridad bajo estática/medición, no atomismo. S5: corpus geométrico, astronómico y neoarquimediano confirmado, con textos de cinemática astronómica atribuidos; ningún locus primario lo sitúa junto a Vasubandhu o Avicena en mereología atomista → «Mereología atomista: `UNSPECIFIED`»; rama geométrica/neoarquimediana pendiente de mejor locus. S3: pistas de mecánica reales pero no promovidas. (D11) |
| Relevancia | F14. Clasificación recomendada por S4: `statics / calibration / equilibrium`, no `atomism / continuum`. |
| Procedencia | S3, S4, S5 |
:::

### E32 · al-Qūhī y al-Sijzī, el «compás perfecto»

::: ficha
| | |
|:--|:-------------|
| Fecha · lengua | s. X–XI · árabe |
| Contenido | Instrumentos y teoría para trazar cónicas de modo continuo; Rashed documenta un capítulo nuevo de teoría geométrica. Al-Qūhī considera «mensurables» las curvas generadas por un único movimiento continuo a las que puede aplicarse la teoría de proporciones; al-Sijzī clasifica curvas según cómo se generan. |
| URL | <https://www.cambridge.org/core/journals/arabic-sciences-and-philosophy/article/abs/alquhi-and-alsijzi-on-the-perfect-compass-and-the-continuous-drawing-of-conic-sections/9C08F654631883D4CDFF486D23437A18> (S3) · <https://www.degruyter.com/> (Rashed / matemática árabe, genérico; solo S5-ES) |
| Estado | Parcial: sin texto árabe abierto con folio/página (S4). |
| Relevancia | Adversario metodológico de Khayyām: el protocolo dinámico de generación determina la clase de objeto geométrico y su mensurabilidad (S3, F10; S5). |
| Procedencia | S3, S4, S5 |
:::

### E33 · Ibn Sīnā, *al-Shifāʾ, al-Samāʿ al-ṭabīʿī* (*Physics*) III.4, 189.14–190.3 — contacto de átomos

::: ficha
| | |
|:--|:-------------|
| Fecha · lengua | 980–1037 · árabe |
| Contenido | Tres átomos x–y–z: si y impide que x y z se toquen, y tiene regiones/contactos distintos y por tanto es divisible; si todos se tocan «completamente», se interpenetran y el agregado no aumenta de magnitud. |
| Edición | McGinnis, *Avicenna*, pp. 75–76 (E35); ed./trad. McGinnis 2009 (E36). |
| URL | <https://www.mercaba.es/islam/fisica_de_avicena.pdf> (S1) |
| Estado | Confirmado directamente (S1). Prioridad H10 máxima (S4). |
| Nota | La semejanza con Vasubandhu es fuerte; no hay evidencia que justifique afirmar transmisión histórica entre ambos (S1). |
| Procedencia | S1, S4, S5 |
:::

### E34 · Ibn Sīnā, *Physics* III.3.15–16 y III.4 §12 — piedra de molino

::: ficha
| | |
|:--|:-------------|
| Locus | S4/S5: *Physics* III.3–4. S1: III.3.15–16: movimiento de círculos próximos al borde y al centro de una piedra de molino. III.4 §12, p. 295 de McGinnis: vuelve sobre él contra el atomismo. |
| Contenido | El exterior recorre mayor intervalo; las alternativas atomistas conducen a saltos o reposos diferentes, separación o fragmentación de la piedra. |
| URL | <https://www.mercaba.es/islam/fisica_de_avicena.pdf> (S1) · edición: E36 |
| Estado | Confirmado con precisión (S1). S1 matiza: «las partes del exterior recorren distancias desiguales y permanecen unidas» da la intuición; el argumento concreto es una reducción al absurdo contra el mínimo/átomos. |
| Relevancia | Cinemática de cuerpo rígido contra la discreción atomista del movimiento (S5). |
| Procedencia | S1, S4, S5 |
:::

### E35 · Jon McGinnis, *Avicenna* (OUP 2010)

::: ficha
| | |
|:--|:-------------|
| Datos | Oxford University Press, 2010; ISBN impreso 978-0-19-533147-9; DOI 10.1093/acprof:oso/9780195331479.001.0001. Cap. 3, «Natural Science», pp. 53–88: movimiento, continuo y argumentos antiatomistas. |
| URL | <https://academic.oup.com/book/3244> |
| Estado | Confirmado. S1: el PDF de UMSL consultado en el transcript [cortado]; usar la ficha OUP como referencia bibliográfica. |
| Procedencia | S1 |
:::

### E36 · Avicenna, *The Physics of The Healing*, ed. y trad. Jon McGinnis (BYU 2009)

::: ficha
| | |
|:--|:-------------|
| Datos | *The Physics of The Healing: A Parallel English-Arabic Text in Two Volumes*, trans., intro. & notes Jon McGinnis, Brigham Young University Press, 2009, ISBN 978-0-8425-2747-7. Libro III, cap. 4 comienza en p. 281. |
| URL | <https://press.uchicago.edu/ucp/books/book/distributed/P/bo10581412.html> |
| Estado | Confirmado bibliográficamente; edición a usar para los dos argumentos (E33, E34) (S1). Conservar los pins III.3.15–16 y III.4 con paginación McGinnis (S4). |
| Procedencia | S1, S4 |
:::

### E37 · ʿUmar Khayyām, tratado sobre las dificultades en los postulados de Euclides

::: ficha
| | |
|:--|:-------------|
| Fecha · lengua | Tratado c. 1070; vida 1048–1131 · árabe |
| Contenido | Al revisar intentos de demostrar el postulado de las paralelas, critica a Ibn al-Haytham por introducir el movimiento de una línea: el movimiento debe excluirse de la geometría (*motion should be excluded from geometry*). Ṭūsī siguió en gran parte esa estrategia. |
| URL | <https://www.iranicaonline.org/articles/khayyam-omar/khayyam-omar-xiv-as-mathematician/> · <https://plato.stanford.edu/entries/umar-khayyam/index.html> |
| Estado | Argumento confirmado; pin árabe crítico parcial (S4). |
| Relevancia | Negativo de Proclo/al-Rāzī: no derivar la estructura estática del espacio de un procedimiento dinámico de generación (S3, F11). |
| Procedencia | S3, S4, S5 |
:::

### E38 · Abū al-Barakāt al-Baghdādī, *Kitāb al-Muʿtabar*

::: ficha
| | |
|:--|:-------------|
| Fecha · lengua | s. XII (vida 1077–1152, S5) · árabe |
| Contenido | Al discutir a Avicena parte de una secuencia observacional: el objeto está en x en un tiempo y en y después, y juzgamos que se movió. Rechaza que el movimiento transversal sea solo la síntesis mental de esos registros: la sucesión tiene realidad extramental aunque sus fases no coexistan. |
| URL | <https://www.cambridge.org/core/journals/arabic-sciences-and-philosophy/article/reception-of-avicennas-theory-of-motion-in-the-twelfth-century/85EF5D5AEDC78A6459C920B02945B39A> |
| Estado | Parcial; falta edición árabe con volumen/página (S4). |
| Relevancia | F12. Avicena y Abū al-Barakāt ofrecen respuestas diferentes dentro del mismo marco (S3, cortado). |
| Procedencia | S3, S4, S5 |
:::

### E39 · Bhāskara II, *Siddhāntaśiromaṇi* (*Siddhānta-śiromaṇi*) — *tātkālika-gati*

::: ficha
| | |
|:--|:-------------|
| Fecha · lengua | c. 1150 · sánscrito |
| Contenido | Distingue la velocidad diaria de una velocidad instantánea (*tātkālika-gati*), necesaria en particular para la Luna y para determinar comienzos/finales de *tithi*, porque la tasa cambia de un momento a otro. Hay literatura especializada sobre la expresión matemática que usa. |
| URL | <https://iks.iitgn.ac.in/wp-content/uploads/2016/02/Indian-Tradition-of-Science-an-Introductory-Overview-MD-Srinivas-Feb-2016.pdf> |
| Estado | Parcial: sin estrofa sánscrita críticamente fijada (S4). |
| Nota | No llamarlo «derivada» sin más ni afirmar influencia; la comparación estructural con Heytesbury es real (S3, S4). |
| Procedencia | S3, S4 |
:::

### E40 · Maimónides, *Guía de perplejos* (*Guide of the Perplexed*; Sefaria: *Guide for the Perplexed*) I.73

::: ficha
| | |
|:--|:-------------|
| Fecha · lengua | c. 1190; vida 1138–1204 · judeoárabe; transmisión hebrea/inglesa |
| Contenido | Expone críticamente las premisas del *kalām*: primera, los cuerpos se componen de átomos indivisibles; tercera, el tiempo se compone de átomos temporales; también el vacío. Movimiento, espacio y tiempo deben discretizarse conjuntamente. |
| Edición | M. Friedländer, traducción inglesa histórica (Sefaria). |
| URL | <https://www.sefaria.org/Guide_for_the_Perplexed%2C_Part_1.73> |
| Estado | Confirmado; es testimonio crítico externo sobre los *mutakallimūn*, no su propia física (S4). |
| Relevancia | Espejo de Aristóteles VI.1: ambos ligan las tres estructuras y escogen ramas opuestas (S2, S5). Alta pertinencia para dinámica discreta (S2). |
| Procedencia | S2, S4, S5 |
:::


### E41 · Fakhr al-Dīn al-Rāzī, *al-Maṭālib al-ʿāliya*, vol. VI

::: ficha
| | |
|:--|:-------------|
| Fecha · lengua | c. 1200 (S4); s. XII–XIII (S5) · árabe |
| Locus | VI, 48–49: esfera que rueda sobre un plano. VI, 52: el extremo puntual de una línea que se desplaza sobre otra toca sucesivamente todos sus puntos (S2). VI, 71: argumento de la semilla de mostaza frente a la divisibilidad ilimitada (S4). (D10) |
| Contenido | Una esfera verdadera toca un plano en un punto indivisible; al rodar, un punto de contacto cesa y comienza otro; la sucesión de contactos indivisibles genera una línea, de donde se infiere la composición puntual de la línea. La SEP distingue estos puntos sin extensión de los átomos griegos extensos. |
| URL | <https://plato.sydney.edu.au/entries/al-din-al-razi/> (SEP; da el pin VI 48–49 y 71) · <https://jisarchive.cis-ca.org/_media/pdf/2006/2/A_avhitkoaaaapstma.pdf> (S2) |
| Estado | Confirmado. |
| Relevancia | Transición contacto estático → movimiento → continuo usada para inferir atomismo (S2, F4). S2 lo propone como primera incorporación a H10/H11; S3 sitúa por delante el bloque jaina. Puente histórico más directo (S4). |
| Procedencia | S2, S4, S5 |
:::

### E42 · Tomás de Aquino (Thomas Aquinas), *Summa contra Gentiles* III.64–77

::: ficha
| | |
|:--|:-------------|
| Fecha · lengua | c. 1260–1270 · latín |
| Contenido | Corpus Thomisticum contiene Liber III, capita 64–110 (incluida la secuencia 64–77); texto leonino revisado por Enrique Alarcón. III.77 trata la ejecución de la providencia mediante causas secundarias. |
| URL | <https://www.corpusthomisticum.org/scg3064.html> (S1) · <https://www.liriocatolico.com.br/suma_contra_gentios/view/SCG3.C77/> (S4) |
| Estado | Referencia real y localizada, pero en el transcript solo aparece como una línea de *checklist* y no se muestra ningún argumento de Aquino en esos capítulos (S1). Mislocated temáticamente (S4). |
| Nota | Mantener solo si H10 necesita causalidad/providencia, no como fuente del continuo (§6, nº 5; F18). |
| Procedencia | S1, S4 |
:::

### E43 · Naṣīr al-Dīn al-Ṭūsī, *al-Tadhkira fī ʿilm al-hayʾa* II.11 (par de Ṭūsī)

::: ficha
| | |
|:--|:-------------|
| Fecha · lengua | c. 1260s; vida 1201–1274 · árabe |
| Contenido | Dos círculos coplanares con radios 2:1, rotaciones opuestas y velocidades angulares 1:2 producen para un punto una oscilación rectilínea sobre el diámetro. La Iranica localiza sus etapas entre la redacción del *Almagest*, la *Moʿīniya* y la *Taḏkera*. |
| Edición | F. Jamil Ragep, *Naṣīr al-Dīn al-Ṭūsī’s Memoir on Astronomy* (*al-Tadhkira fī ʿilm al-hayʾa*), 2 vols., Springer, 1993, árabe/inglés; Book II, ch. 11. |
| URL | <https://wellcomecollection.org/works/s6gufpfm> · <https://www.davidboeno.org/GROEUVRE/CONIQUES/tusiII11.html> · <https://www.iranicaonline.org/articles/tusi-nasir-al-din-mathematician-astronomer/> |
| Estado | Confirmado con pin (Book II, ch. 11). Prioridad H10/H11 alta. |
| Relevancia | Invierte «un punto móvil genera una línea»: un registro cinemático simple es producido por una dinámica latente más compleja; la descomposición causal no viene dada por la trayectoria (F16; *identifiability*). |
| Procedencia | S3, S4, S5 |
:::

### E44 · Juan Duns Escoto, *Ordinatio* II, d.2, p.2, q.5

::: ficha
| | |
|:--|:-------------|
| Fecha · lengua | c. 1300 · latín |
| Locus | nn. 284–376. nn. 287–292 (S4) / 289–292 (S1): si un continuo/sucesivo puede componerse de indivisibles. n. 289: qué sucede inmediatamente a un indivisible. n. 291: lo absolutamente mínimo no es cuantitativo. n. 292: conecta magnitud, tiempo y movimiento siguiendo *Physics* VI. Hasta n. 376: solución que entiende punto/instante no como cosa positiva que compone el continuo. (D09) |
| Edición | Transcripción latín/inglés con numeración crítica (Logic Museum). Vivès, *Opera omnia*: la serie comenzó en 1891 («Vives 1891–95»); II d.1–2 está en el tomus XI, París: Ludovicus Vivès, 1893. |
| URL | <https://www.logicmuseum.com/wiki/Authors/Duns_Scotus/Ordinatio/Ordinatio_II/D2/P2Q5> · <https://openlibrary.org/works/OL15847667W/Opera_omnia> |
| Estado | Confirmado. Contenido confirmado, pero el nombre de archivo necesita corrección bibliográfica (S1). |
| Nota | Archivo local `Scotus_OpusOxoniense_II_d2_Vives1891…` → `Scotus_Ordinatio_II_d2_Vives1893…`, o metadato que distinga la serie (1891) del tomo XI (1893) (S1, S4, S5). S5-EN describe los argumentos como geométricos. |
| Procedencia | S1, S4, S5 |
:::

### E45 · Henry of Harclay, *Quaestiones ordinariae*

::: ficha
| | |
|:--|:-------------|
| Fecha · lengua | c. 1310s; vida c. 1270–1317 · latín |
| Contenido | Reutiliza la problemática de *De lineis indivisibilibus* (E13). Sostiene que un continuo infinitamente divisible puede estar compuesto de indivisibles, y por ello debe reconstruir qué significa que los indivisibles «se toquen». |
| Edición | Mark G. Henninger (ed.), Raymond Edwards & Henninger (trad.), *Henry of Harclay: Ordinary Questions*, OUP, 2008. |
| Estudio | Crialesi, «La recepción latina medieval del pseudoaristotélico *Sobre las líneas indivisibles*: reevaluación del estado de la cuestión», *Revista Española de Filosofía Medieval*, DOI 10.21071/refime.v29i2.14564 (recepción del pseudo-Aristóteles y contraste con Wodeham). |
| URL | <https://journals.uco.es/refime/article/view/14564> · <https://plato.stanford.edu/archives/sum2010/entries/walter-chatton/> (S3, fila Harclay/Chatton) |
| Estado | Confirmado a nivel doctrinal; falta registrar *quaestio*/página en H10 (S4). |
| Relevancia | Distinción «divisible por puntos» / «compuesto de puntos»: una base de descomposición puede ser completa sin ser la ontología de piezas (S3, S5). |
| Procedencia | S3, S4, S5 |
:::

### E46 · Walter Chatton

::: ficha
| | |
|:--|:-------------|
| Fecha · lengua | c. 1320s–1330s; vida 1290–1343 · latín |
| Contenido | Un continuo finito tiene un máximo potencial de divisiones finitas, pero esos indivisibles no existen como cuentas de un collar antes de componerlo; «componen» solo en sentido reducido/potencial. El análisis mediante indivisibles no equivale a indivisibles preexistentes yuxtapuestos. |
| URL | <https://plato.stanford.edu/entries/walter-chatton/> (S5) · <https://plato.stanford.edu/archives/sum2010/entries/walter-chatton/> (S3) |
| Estado | Parcial: sin edición primaria/pin comparable a Scotus o Wodeham (S4). |
| Relevancia | Descomposición analítica sin ontología ingenua de piezas (S5). |
| Procedencia | S3, S4, S5 |
:::

### E47 · Adam Wodeham, *Tractatus de indivisibilibus*

::: ficha
| | |
|:--|:-------------|
| Fecha · lengua | c. 1330s; vida c. 1298–1358 · latín |
| Contenido | El debate no trataba solo de átomos corporales: incluye puntos matemáticos, instantes temporales y *mutata esse* (indivisibles del movimiento). Wodeham defiende frente a Harclay/Chatton la divisibilidad indefinida; rechaza soluciones indivisibilistas y extiende el problema a línea, tiempo y movimiento. Pieza central de la recepción latina del pseudo-Aristóteles. |
| Edición | Rega Wood, *Adam de Wodeham: Tractatus de Indivisibilibus. A Critical Edition, Introduction, Translation, and Textual Notes*, Synthese Historical Library 31, Dordrecht/Boston/London: Kluwer, 1988, pp. vii + 333, ISBN 90-277-2424-5 (reseña BJHS; precio indicado £74.00). |
| URL | <https://www.cambridge.org/core/journals/british-journal-for-the-history-of-science/article/abs/adam-de-wodeham-tractatus-de-indivisibilibus-a-critical-edition-introduction-translation-and-textual-notes-by-rega-wood-synthese-historical-library-volume-31-dordrecht-boston-london-kluwer-academic-publishers-1988-pp-vii-333-isbn-9027724245-7400/892EB67EFB311772A40BD5C5611BEDFA> · <https://link.springer.com/book/10.1007/978-94-009-1425-4> (S3) |
| Estado | Confirmado bibliográfica y temáticamente. |
| Relevancia | Paralelismo técnico espacio–tiempo–movimiento semejante al de Aristóteles y el *kalām* (S3, S5). |
| Procedencia | S3, S4, S5 |
:::

### E48 · William Heytesbury, *Regulae solvendi sophismata*, caps. IV–VI

::: ficha
| | |
|:--|:-------------|
| Fecha · lengua | c. 1335; vida c. 1313–1372 · latín |
| Contenido | Límites temporales y posiciones instantáneas funcionan como límites; el cap. VI trata velocidad y aceleración. La velocidad de un movimiento no uniforme en un instante se mide por la distancia que recorrería el móvil si durante algún intervalo continuase uniformemente con aquel grado (S3, S5). |
| Edición | Facsímil del incunable de Venecia 1491, Universidad de Salamanca. |
| URL | <https://plato.stanford.edu/entries/heytesbury/> · <https://gredos.usal.es/handle/10366/84387> · <https://bibnum.publimath.fr/ACF/ACF08001.pdf> (S3) |
| Estado | Confirmado en estructura; la formulación contrafactual necesita folio antes de citarse entre comillas (S4) (D30). |
| Relevancia | Magnitud instantánea definida mediante un experimento contrafactual de referencia, no mediante la distancia recorrida en el instante; no llamarlo simplemente «la derivada moderna» (S3, cortado; S5). |
| Procedencia | S3, S4, S5 |
:::

### E49 · Bonaventura Cavalieri, *Geometria indivisibilibus continuorum nova quadam ratione promota* (1635)

::: ficha
| | |
|:--|:-------------|
| Fecha · lengua | 1635; vida 1598–1647 · latín |
| Contenido | Compara superficies por «todas sus líneas» y sólidos por «todos sus planos». Terminó evitando comprometerse con que el continuo esté literalmente compuesto de ellos: el método necesita correspondencia y proporción, no ontología composicional. |
| URL | <https://plato.stanford.edu/entries/continuity/index.html> (S2) · <https://plato.stanford.edu/entries/continuity/> (S5) |
| Estado | Confirmado; edición digital primaria por normalizar; acompañar en H11 con estudios de la controversia sobre indivisibles (S4). |
| Relevancia | Exhaustividad operacional sin compromiso mereológico fuerte (S2, S5). |
| Procedencia | S2, S4, S5 |
:::

### E50 · Galileo, *Discorsi e dimostrazioni matematiche intorno a due nuove scienze* (1638), Prima giornata

::: ficha
| | |
|:--|:-------------|
| Fecha · lengua | 1638; vida 1564–1642 · italiano |
| Contenido | Reutiliza la rueda (E12) contra el continuo: una línea puede considerarse resuelta en infinitos indivisibles; explica la diferencia de recorridos introduciendo infinitos *vacua* indivisibles entre los puntos correspondientes de la circunferencia menor. |
| Edición | Edición original Leiden, Elsevier, 1638; la discusión está en la Primera Jornada (*Prima giornata*). S4 recomienda facsímil de 1638 o Edizione Nazionale en lugar de transcripción web. |
| URL | <https://falsafa.ai/works/galileo-galilei-dialogues-concerning-two-new-sci-8eceb2/05-two-new-sciences-by-galileo-first-day-interlocutor/translation/> (S2) |
| Estado | Confirmado. |
| Relevancia | Paradoja cinemática convertida en teoría de la microestructura del espacio (S2, S5). |
| Procedencia | S2, S4, S5 |
:::

### E51 · Choe Seok-jeong 崔錫鼎, *Gusuryak* 九數略

::: ficha
| | |
|:--|:-------------|
| Fecha · lengua | c. 1700, Corea/Joseon; vida «1664–?» según S5 (D15) · chino clásico usado en Corea |
| Contenido | Construcciones combinatorias y el *jisugwimundo*; arreglos asociados hoy con cuadrados latinos. Sin argumento sobre continuo, contacto o registro comparable con Liu Hui/Takebe en esta pasada. |
| Custodia | Kyujanggak Institute for Korean Studies. |
| URL | <https://en.wikipedia.org/wiki/Choi_Seok-jeong> · <https://mathsci.kaist.ac.kr/home/en/2018/09/opening-of-choi-seok-jeong-seminar-room/> |
| Estado | Auténtico, pero temática débil; no forzar dentro de H10 (S4). S5: analogía estructural (variables locales bajo restricciones globales de compatibilidad), no atomismo ni teoría del continuo. |
| Nota | Dejar en una carpeta de matemática coreana salvo que una lectura primaria revele un pasaje geométrico pertinente (S4). |
| Procedencia | S4, S5 |
:::

### E52 · Hong Jeong-ha

::: ficha
| | |
|:--|:-------------|
| Fecha | vida 1684–? (S5) |
| Contenido | Matemática algorítmica: paralelos laterales sobre construcción y verificación paso a paso; no se estableció argumento primario sobre atomismo o continuo. Sin obra, locus ni URL en la fuente. |
| Estado | Analogía lateral (S5). |
| Procedencia | S5 |
:::

### E53 · Takebe Katahiro, *Tetsujutsu Sankei* (1722)

::: ficha
| | |
|:--|:-------------|
| Fecha · lengua | 1722; vida 1664–1739 · japonés/kanbun matemático |
| Contenido | Cortar uniformemente el diámetro produce segmentos de circunferencia desiguales y números «disobedient to the attribute» del círculo. Prefiere polígonos inscritos que dividen uniformemente la circunferencia y aplica después su procedimiento de aceleración de convergencia; obtuvo unas 40 cifras de π. |
| URL | <https://mathshistory.st-andrews.ac.uk/Biographies/Takebe/> |
| Estado | Parcial a nivel de edición (sin página de edición japonesa); comparación metodológica fuerte (S4). |
| Relevancia | No toda discretización interroga igual al objeto; observables/discretización adaptados al invariante antes de extrapolar el límite (S3, F13). S3 lo considera el hallazgo metodológico más aprovechable. |
| Procedencia | S3, S4, S5 |
:::

### E54 · Hong Dae-yong 洪大容, *Ŭisan mundap* 醫山問答

::: ficha
| | |
|:--|:-------------|
| Fecha · lengua | c. 1760s–1770s (cronograma de S4: 1766) · chino clásico coreano |
| Contenido | *Questions and Answers on Mount Yiwulu*: rotación terrestre (`地轉說`), astronomía, matemáticas y un universo no organizado alrededor de un centro cultural chino. |
| Edición | *Imha kyŏngnyun, Ŭisan mundap*, Konkuk University Press, 1975 (incluye el original chino); si es posible, facsímil de *Damhŏnsŏ*. |
| URL | <https://klwave.or.kr/klw/directories/200300/authorsView.do> (LTI Korea / KLWAVE) · <https://openlibrary.org/works/OL33545816W/Imha_ky%C5%8Fngnyun_%C5%ACisan_mundap> |
| Estado | Confirmado a nivel de obra/doctrina; falta pin de línea en el original. |
| Relevancia | F15. Obliga a distinguir movimiento observado de elección de referencia cosmológica. |
| Procedencia | S4 |
:::

### E55 · Choe Han-gi 崔漢綺, *Gicheukcheui* 氣測體義 (1836): *Singitong* 神氣通 y *Ch'uch'ŭkrok* 推測錄

::: ficha
| | |
|:--|:-------------|
| Fecha · lengua | 1836; vida 1803–1877 · chino clásico coreano |
| Contenido | *Gicheukcheui* integra *Singitong* y *Ch'uch'ŭkrok* (variantes de romanización: *Ch'uch'ŭngnok*, *Ch'uch'ŭk-rok*). El segundo tiene seis agrupaciones, entre ellas `推動測靜`, treinta secciones dedicadas nominalmente a `動` y `靜` (movimiento y reposo); título en torno a inferir movimiento / medir o examinar reposo. |
| Edición | Reproducción moderna *神氣通, 推測錄, 習算津筏*, Sungkyunkwan University Daedong Institute, 1971. La bibliografía coreana actual trabaja directamente con *Gicheukcheui*. |
| URL | <https://books.google.com/books/about/%E7%A5%9E%E6%B0%A3%E9%80%9A_%E6%8E%A8%E6%B8%AC%E9%8C%84_%E7%BF%92%E7%AE%97%E6%B4%A5%E7%AD%8F.html?id=bGY_zgEACAAJ> · <https://www.namu.moe/w/%EA%B8%B0%EC%B8%A1%EC%B2%B4%EC%9D%98> · <https://en.wikipedia.org/wiki/Choe_Han-gi> · <https://encykorea.aks.ac.kr/Article/E0057904> (Academy of Korean Studies; S5) |
| Estado | S4: bibliografía confirmada; interpretación de pasaje parcial; no leer el título como teoría de *measurement* hasta cotejar las treinta unidades. S5: afirma que la sección articula inferencia de lo estático a partir de lo móvil y que la obra desarrolla una epistemología de observación, inferencia y acumulación de conocimiento, sin citar pasaje. S3: no promovido. (D12) |
| Nota | No escribir en `IDEA_BRIDGES.md` «Choe Han-gi anticipates inference of dynamics from static measurement». Estado operativo: target confirmado; tesis técnica no confirmada (S4). |
| Procedencia | S3, S4, S5 |
:::

### E56 · Choe Han-gi, obras posteriores

::: ficha
| | |
|:--|:-------------|
| Obras | *Kihak* 氣學 (1857); *Unhwa ch'ŭkhŏm* 運化測驗 (1860); *Sŏnggi unhwa* (1867). |
| Contenido | Filosofía de *gi* en actividad continua; intento de integrar conocimientos mecánicos/cosmológicos importados con una teoría causal propia. |
| URL | <https://en.wikipedia.org/wiki/Choe_Han-gi> |
| Estado | Confirmado bibliográficamente; pins primarios pendientes. |
| Procedencia | S4, S5 |
:::

### E57 · Simon Kochen & Ernst P. Specker, «The Problem of Hidden Variables in Quantum Mechanics»

::: ficha
| | |
|:--|:-------------|
| Datos | *Journal of Mathematics and Mechanics* 17, 59–87. Cita convencional 1967; la página DOI actual de Indiana etiqueta 1968 y el DOI contiene 1968: 10.1512/iumj.1968.17.17004. |
| URL | <https://cds.cern.ch/record/429520> · <https://doi.org/10.1512/iumj.1968.17.17004> |
| Estado | Confirmado; conservar ambas fechas con nota editorial. |
| Relevancia | Imposibilidad de asignar simultáneamente valores no contextuales a todos los observables del tipo requerido: paralelo moderno para «qué propiedades pueden coexistir en una misma estructura estática de medida». No es genealogía histórica; no «confirma» a Mohistas, Vasubandhu ni Dignāga. Ubicación: H11, `structural analogy — no transmission claim` (S4). |
| Procedencia | S1, S4 |
:::

### E58 · *Ratnagotravibhāga* (*Mahāyānottaratantraśāstra*), I.154–155 / I.157–158

::: ficha
| | |
|:--|:-------------|
| Numeración | I.154–155 en la edición/traducción presentada por Tsadra; I.157–158 en otras bibliografías. |
| Contenido | El elemento está vacío de manchas adventicias separables y no vacío de cualidades insuperables inseparables. |
| URL | <https://buddhanature.tsadra.org/index.php/Texts/Ratnagotravibh%C4%81ga_Mah%C4%81y%C4%81nottaratantra%C5%9B%C4%81stra/English> |
| Estado | Pasaje localizado; numeración dependiente de edición. Guardar texto sánscrito crítico + variante de numeración (S4). |
| Relevancia | Comparación formal con: ¿qué propiedades pertenecen intrínsecamente al portador y cuáles dependen de relaciones/condiciones? No convierte el *tathāgatagarbha* en átomo ni muestra recepción aristotélica. §4.4. |
| Procedencia | S4 |
:::

### E59 · *Śrīmālādevīsiṃhanāda*

::: ficha
| | |
|:--|:-------------|
| Contenido | Autoridad que el propio RGV invoca para la distinción «vacío de X / no vacío de Y»: el *tathāgatagarbha* está vacío de las envolturas separables de las aflicciones y no separado de cualidades búdicas inconcebibles. No es el *Heart Sūtra*. |
| URL | <https://buddhanature.tsadra.org/index.php/Articles/All_Buddhas_and_All_Living_Beings_Are_Just_This_One_Mind> |
| Estado | Citado vía Tsadra; sin pin propio. |
| Procedencia | S4 |
:::


# 4. *Heart Sūtra*, *Dao De Jing* 14, *tathāgatagarbha* y atomismo griego

## 4.1 Planteamiento

La búsqueda «*Heart Sūtra* + *tathāgatagarbha* + TTC 14 + “propiedades aristotélicas de los átomos”» produjo sobre todo una corrección (S4). Hay paralelos verbales y conceptuales comparables: imperceptibilidad sensorial en TTC 14; ausencia de características, nacimiento y cese en el *Heart Sūtra*; propiedades adventicias separables frente a inseparables en el RGV. No se encontró fuente académica que documente una relación histórica entre esos pasajes y el atomismo griego. «Propiedades aristotélicas de los átomos» es etiqueta errónea (E04).

Cuatro textos a no fundir (S4): TTC 14 (E02) — sujeto: el Dao; *Heart Sūtra* (E28) — análisis de la falta de existencia intrínseca de categorías de experiencia y doctrina, no «un objeto microscópico + una lista de sus propiedades físicas»; *Tathāgatagarbha Sūtra* (E22) — naturaleza búdica oculta por condiciones adventicias; RGV (E58) — el pasaje pertinente para propiedades.

S5 añade el pasaje de los sentidos del *Heart Sūtra* (`無眼耳鼻舌身意；無色聲香味觸法`) como eje de la comparación con TTC 14 (vínculo sugerido por el usuario): la semejanza es real a nivel de inaccesibilidad sensorial y de estructura de la observabilidad.

## 4.2 Comparaciones alegadas (S4)

| Comparación | Parecido real | Diferencia | Veredicto |
|:--------|:----------|:-------------|:--------|
| TTC 14 ↔ átomo griego | Imperceptibilidad por vista/tacto; vocabulario de `微` «sutil/fino». | TTC 14 habla del Dao unificado, sin forma ni frente/espalda; no de una pluralidad de corpúsculos con figura, posición y movimiento. | Paralelo poético/fenomenológico; no atomismo. |
| *Heart Sūtra* ↔ átomo | Negación de características intrínsecas y de categorías ordinarias de aparición. | El sutra vacía de naturaleza propia forma, agregados, sentidos y dharmas; no postula unidades físicas imperceptibles. | Comparación filosófica posible; equivalencia física falsa. |
| *tathāgatagarbha*/RGV ↔ «propiedades esenciales del átomo» | Condiciones adventicias separables frente a rasgos presentados como inseparables. | Objeto de la doctrina: *buddha-nature*/*dharmadhātu*, no materia mínima; marco soteriológico. | Analogía mereológica/predicativa, no histórica. |
| Aristóteles ↔ los tres anteriores | Pregunta general por qué predicados pertenecen a una cosa y qué puede percibirse de ella. | La física aristotélica del continuo es anticomposición por puntos; la teoría atómica descrita es democritea. | No hay «eco aristotélico de átomos» demostrado. |

## 4.3 Rasgos comparados (S5)

| Rasgo | *Heart Sūtra* | TTC 14 | Atomismo griego (según Aristóteles) |
|:--------|:----------|:----------|:----------|
| Inaccesibilidad sensorial ordinaria | Sí, dentro de una crítica de la reificación / de los dharmas | Sí, explícita | Compatible, pero no es el criterio definitorio |
| No surgir / no cesar | Sí (`不生不滅`) | No es la fórmula central | Átomos normalmente ingenerados e imperecederos |
| Figura determinada | No; no hay teoría corpuscular | Forma ordinaria negada o inaccesible | Sí |
| Orden y posición | No son el núcleo | La orientación ordinaria se vuelve elusiva (sin frente ni espalda) | Sí |
| Función | Vacuidad / crítica de los dharmas | Dao no objetualizable | Constituyentes materiales |

Rasgos listados por S5 para cada texto. *Heart Sūtra*: vacuidad de los cinco *skandhas* (S5-EN) / de los dharmas (S5-ES); «no nacer / no cesar»; «no aumentar / no disminuir»; negación analítica de las facultades sensoriales y sus objetos. TTC 14: mirar y no ver; escuchar y no oír; intentar asir y no obtener; forma de lo sin forma; imagen de lo que no es cosa. Atomismo: átomos que difieren por figura, orden y posición.

Conclusión S5: semejanza estructural interesante, identidad ontológica no demostrada, ninguna transmisión histórica demostrada.

## 4.4 RGV y propiedades (diagrama de S4 como tabla de aristas)

| Origen | Relación | Destino |
|:----------|:----------|:----------|
| Propiedades adventicias | separables | Portador / objeto |
| Propiedades inseparables | atribuidas como inseparables | Portador / objeto |
| Portador / objeto | → | Registro observado |
| Contexto de medida | → | Registro observado |

La similitud termina en la estructura: la autoridad citada por el RGV es la *Śrīmālādevīsiṃhanāda* (E59). No se encontró evidencia de que el pasaje derive del *Heart Sūtra*, del *Dao De Jing* ni de Aristóteles.

## 4.5 Resultado negativo

No se encontró publicación filológica o de historia de la ciencia que establezca la cadena Leucipo/Demócrito/Aristóteles → TTC 14 → *Heart Sūtra*/*tathāgatagarbha*; en internet solo hay comparaciones generales entre Dao, vacuidad y filosofías occidentales. Registro para el repositorio:

> `No evidence found for historical Aristotelian-atomist transmission to DDJ 14, Heart Sutra, or tathāgatagarbha texts; comparison only.`

Estado: *comparison hypothesis rejected / no transmission evidence found*. Ubicación: apéndice comparativo epistemológico (S5), no evidencia atomista.

# 5. Reordenación temática (S4)

| Eje | Referencias primarias más fuertes | Qué aportan | Prioridad |
|:------|:-------------|:----------------|:------|
| C · Contacto y continuidad | Zenón/Simplicio; Aristóteles *Phys.* VI.1; *Mohist* A61/A69; Nyāya 4.2.23–25; Vasubandhu AKBh I.43d y *Viṃśatikā* 12; Epicuro §§58–59; Scotus II d.2 q.5; Wodeham | Distinguen punto/límite/átomo, contacto total o parcial, contigüidad, partes, divisibilidad y emergencia de extensión. Aristóteles niega que puntos compongan el continuo; los Mohistas dan función estructural positiva al extremo sin espesor; Vasubandhu fuerza la alternativa «contactos distintos → partes / mismo contacto → colapso espacial». | Máxima |
| M · Movimiento desde puntos / registros sucesivos | *Zhuangzi* 33; Nāgārjuna II; al-Naẓẓām; al-Rāzī VI.48–49; Proclo; Ps.-*Mechanica* 24; Ṭūsī II.11; Galileo | Qué convierte una sucesión de posiciones/contactos en movimiento y qué estructura dinámica puede estar oculta bajo una trayectoria observada. | Máxima |
| S · Medición, equilibrio y secciones | Arquímedes *Method* 2; Liu Hui; Zu Geng; Thābit; Cavalieri; Takebe | Una familia exhaustiva de relaciones locales o secciones fija una magnitud global. Thābit: configuración de equilibrio como requisito para que una lectura instrumental sea válida. Liu Hui y Takebe: dependencia respecto del esquema de aproximación. | Muy alta |
| B · Mereología y *binding* | *Mohist* A2/A61/A69; *Tattvārthasūtra* 5.11/14/32–33; Nyāya *avayavin*; Epicuro | Separan ser partes, ocupar lugar, ser contiguo y constituir un solo compuesto. Jainismo: más constituyentes no implican más *pradeśas*; co-ubicación no equivale a *bandha*. | Máxima |
| R · Epistemología de registros | Dignāga AP 1–2; *Heart Sūtra*; Heytesbury; Hong Dae-yong; Choe Han-gi; Kochen–Specker | Separar causa física, contenido representado, marco de referencia, propiedad inferida y contexto compatible de medida. La conexión con contextualidad es analógica/formal, no genealogía. | Muy alta |
| P · Propiedades intrínsecas/adventicias | RGV I.154–155; *Śrīmālādevī*; comparativamente Aristóteles/Demócrito | Distinción explícita entre lo separable y lo declarado inseparable del portador. Contraste conceptual, no física atomista. | Media-alta, como puente conceptual |
| G · Geometría estática frente a generación dinámica | Proclo; Khayyām; al-Qūhī/al-Sijzī; al-Rāzī; Ṭūsī | Respuestas incompatibles a: ¿puede definirse/demostrarse una estructura espacial mediante el proceso que la genera? | Alta, una vez completados los pins árabes |

# 6. Correcciones para las notas del repositorio

Consolidación de S1 (dos correcciones y una advertencia) y S4 (diez), más la política de etiquetas de S5.

| Nº | Objeto | Corrección | Origen |
|:--|:------|:----------------------|:--|
| 1 | Liu Hui | No usar una sola nota `NineChapters_juan1_LiuHui_circle_cutting…` como soporte del círculo y del resto decreciente de la disección sólida. El círculo: `割之彌細，所失彌少` e iteración del corte. La afirmación «shrinking remainder in solid dissection» se apoya en el *yangma* del *Shanggong*, Sibu Congkan pp. 18–19. Dos notas separadas (E19, E20). | S1, S4 |
| 2 | Mohistas | Dos entradas: `MohistCanon_A61_A69_endpoint_contiguity` (geometría/mereología estática) y `MohistCanon_B17_shadow_replacement` (óptica, persistencia de un efecto observado). No agrupar bajo «Mohist paradoxes». Edición común: Schemmel–Boltz. | S4 (S2) |
| 3 | Schemmel–Boltz | Citar **Schemmel & Boltz 2022**; «electronic publication 2023» solo como fecha de versión digital. DOI 10.1007/978-3-031-08797-4. | S1, S4 |
| 4 | Scotus | De «Opus Oxoniense II d.2, indivisibles» a *Ordinatio* II, d.2, p.2, q.5, nn. 287–292, hasta n. 376. Renombrar `Scotus_OpusOxoniense_II_d2_Vives1891…` → `Scotus_Ordinatio_II_d2_Vives1893…`, o anotar que «Vives 1891–95» designa la serie y el tomo XI es de 1893. | S1, S4 |
| 5 | Aquinas | `SCG III.64–77` no debe figurar como evidencia del problema de los indivisibles sin razón específica; III.77 trata de providencia y causas secundarias. | S1, S4 |
| 6 | al-Shahrastānī / Haarbrücker | Mantener el PDF alemán de 1850 como testigo histórico y herramienta OCR; no como autoridad final para traducir la *ṭafra*. Añadir edición árabe y traducción académica posterior antes de usar sus palabras como cita; conservar el carácter doxográfico. | S1, S4 |
| 7 | Thābit | Nota nueva, no junto a `atom-contact`. Categoría `statics/equilibrium/measurement-instrument`; fuentes `Thabit_Sifat_al-wazn` y `Thabit_Kitab_fi_l-qarastun_BL_IO_Islamic_461_ff198v-207r`. (S5 discrepa en la clasificación: D11.) | S4 |
| 8 | *Tattvārthasūtra* / RGV | No almacenar solo «5.33 binding»: guardar `snigdharūkṣatvād bandhaḥ` + edición + numeración (5.32 en algunas ediciones). RGV: I.154–155 en una numeración, I.157–158 en otra. | S4 |
| 9 | Bloque *Heart*/TTC/Aristóteles | Anotar como resultado negativo (§4.5). Sustituir «Aristotelian atom properties» por «Democritean atomism as reported and criticized by Aristotle». | S4 |
| 10 | Corea | No usar *Gusuryak* como relleno geográfico. Incorporar: `HongDaeyong_UisanMundap_earth_rotation` — confirmado; `ChoeHangi_Chucheukrok_ChudongCheukjeong` — target, passage verification pending; `Woncheuk_HeartSutra_commentary` — target, CBETA/SAT pinpoint pending. | S4 |
| 11 | Artefactos internos | Paths, hashes SHA-256, archivos H08/H09/H10, R11/R12, `IDEA_BRIDGES.md`: son artefactos internos, no referencias externas. El transcript prueba que se consultaron pero no contiene sus contenidos: no han sido auditados. La traza identifica Haarbrücker, Scotus y Aquinas como archivos de fuente locales. | S1 |
| 12 | Etiquetas de estado | Cada nota lleva `PRIMARY EXACT`, `PRIMARY INDIRECT`, `SECONDARY CONFIRMED` o `UNSPECIFIED`, para que las analogías no se conviertan con el tiempo en afirmaciones históricas más fuertes que las fuentes. Prioritario para: Thābit; *Heart Sūtra* ↔ TTC 14; Choe Han-gi; al-Naẓẓām; Takebe; Heytesbury; material coreano y comparaciones interculturales. | S5 |

Balance de S1: ninguna referencia histórica central del transcript resultó inventada; hubo imprecisiones de localización/edición (Liu Hui, Scotus, fecha Schemmel–Boltz) y una advertencia textual sobre Haarbrücker.


# 7. Plan de ingestión H10 / H11

## 7.1 Dos definiciones incompatibles (D13)

| Fuente | H10 | H11 |
|:--|:--------------|:--------------|
| S4 | Corpus de fuentes primarias y argumentos estructurales: ¿qué problema demuestra o formula exactamente la fuente histórica? | Puente estructural, interpretativo: ¿qué pregunta moderna sugiere sin alegar anticipación? Cada entrada con etiqueta `structural analogy — no transmission claim`. |
| S5 | Estructura estática, contacto y composición. | Dinámica, generación y medición. |

Las fuentes no resuelven la diferencia. Se conservan ambas asignaciones (índice §2, columna «Ingestión»).

## 7.2 Ingestión priorizada para H10 (S4)

| Prior. | Archivo sugerido | Fuente que conservar | Razón |
|:--|:----------------|:--------------|:----------|
| A | `Aristotle_Physics_VI1_231a21-231b18_grc_eng.md` | Texto griego crítico + Bekker + traducción moderna; respaldo online. | Base abstracta para continuo/contacto/sucesión. |
| A | `MohistCanon_A61_A69_endpoint_contiguity.md` | Schemmel & Boltz 2022, DOI 10.1007/978-3-031-08797-4. | Límite sin extensión ≠ constituyente; contigüidad positiva. |
| A | `Vasubandhu_Vimsatika_11-15_atom_contact.md` | GRETIL sánscrito + edición Lévi / correcciones posteriores. | La prueba de los seis contactos con texto sánscrito. |
| A | `NyayaSutra_4.2.23-25_atom_parts_contact.md` | Sánscrito Univ. de Delhi + traducción crítica. | Respuesta realista al mismo dilema. |
| A | `Tattvartha_5.11_5.14_binding_pradesa.md` | Sūtra + *Sarvārthasiddhi*; *incipits* además de numeración. | Separa *occupancy*, pluralidad y *binding*. |
| A | `LiuHui_circle_cutting_263.md` | Facsímil chino + edición crítica. | Refinamiento y pérdida. |
| A | `LiuHui_yangma_bienao_dissection_263.md` | Facsímil *Shanggong* separado. | Resto sólido decreciente; evita la mislocalización actual. |
| A | `IbnSina_Physics_III3_III4_atom_millstone.md` | McGinnis, árabe-inglés, BYU 2009. | Dos argumentos: uno estático, otro cinemático. |
| A | `FakhrRazi_Matalib_VI_48-49_rolling_sphere.md` | Árabe crítico + traducción de VI.48–49; registrar VI.71. | Contactos instantáneos → línea. |
| A | `Thabit_Qarastun_IOIslamic461_ff198v-207r.md` | Facsímil BL/Qatar + Abattouy 2001, DOI 10.1017/S0269889701000084. | Eje estática–calibración–medida. |
| A | `Tusi_Tadhkira_II11_couple.md` | Ragep 1993, árabe/inglés, II.11. | Dinámica latente no identificable desde la forma de la trayectoria. |
| B | `Scotus_Ordinatio_II_d2_p2_q5_287-376.md` | Texto crítico + numeración nn. 287–376. | Más preciso que el archivo Vives genérico. |
| B | `Wodeham_Tractatus_indivisibilibus_Wood1988.md` | Rega Wood 1988. | Recepción latina sistemática. |
| B | `HeartSutra_Toh531_T251_empty_form.md` | 84000 Toh 531 + CBETA/SAT T251. | Fuente de vacuidad, con nota explícita «not atomism». |
| B | `Ratnagotravibhaga_I154-155_empty_not_empty.md` | Sánscrito crítico + variante I.157–158. | Propiedades separables/inseparables. |
| B | `HongDaeyong_UisanMundap_motion_frame.md` | Edición 1975 con original chino; si es posible facsímil de *Damhŏnsŏ*. | Marco de interpretación del movimiento. |
| C | `ChoeHangi_Chucheukrok_chudong_cheukjeong.md` | Reproducción Sungkyunkwan 1971; localizar los treinta apartados `推動測靜`. | Lectura requerida antes de promover. |
| C | `Woncheuk_HeartSutra_commentary.md` | CBETA/SAT + edición académica moderna. | Conexión Corea ↔ vacuidad/representación. Lectura requerida. |

Otras notas de repositorio propuestas en S4 (§6): `MohistCanon_B17_shadow_replacement`, `Thabit_Sifat_al-wazn`, `Thabit_Kitab_fi_l-qarastun_BL_IO_Islamic_461_ff198v-207r`, `HongDaeyong_UisanMundap_earth_rotation`, `ChoeHangi_Chucheukrok_ChudongCheukjeong`, `Woncheuk_HeartSutra_commentary`.

## 7.3 H11 según S4

Conexiones modernas separadas, con etiqueta `structural analogy — no transmission claim`: Kochen–Specker (E57); distinción dignaguiana causa/objeto representado (E27); comparación con esquemas de discretización de Takebe (E53); pregunta general por *identifiability*. Kochen–Specker demuestra una restricción matemática sobre asignaciones de valores a observables; no confirma históricamente a Mohistas, Vasubandhu o Dignāga.

## 7.4 División según S5

| H10 — estructura estática, contacto, composición | H11 — dinámica, generación, medición |
|:----------------------|:----------------------|
| Aristóteles, *Physics* VI.1 | Nāgārjuna, *MMK* II |
| Aristóteles sobre Leucipo/Demócrito, *Metaph.* I.4 | *Mohist* B17 |
| Epicuro §§56–59 | Liu Hui: círculo |
| *Mohist* A61/A69 | Liu Hui: sólidos |
| Nyāya 4.2.23–25 | Zu Gengzhi |
| *Tattvārthasūtra* 5.11/5.14/5.33 ss. | Proclo |
| Vasubandhu, *Viṃśatikā* 11–13 | Arquímedes, *Method* prop. 2 |
| Dignāga, *Ālambanaparīkṣā* 1–2 | Ibn Sīnā: piedra de molino |
| Ibn Sīnā, *Physics* III.4 | Maimónides I.73 |
| Duns Scotus, *Ordinatio* II d.2 p.2 q.5 | Fakhr al-Dīn al-Rāzī |
| Henry of Harclay | Ṭūsī |
| Walter Chatton | Heytesbury · Cavalieri · Takebe · Choe Han-gi |

Fuera de ambas listas en S5: Thābit (rama geométrica/neoarquimediana pendiente de mejor locus mereológico); *Heart Sūtra* y TTC 14 (apéndice comparativo epistemológico).

# 8. Método, candidatos no promovidos y trabajo pendiente

## 8.1 Método de las pasadas

Orden aplicado en S2–S4: primero candidatos por asociación («desde los pesos»), tratados como hipótesis de localización; después búsqueda de texto primario o edición académica próxima; descarte o ajuste de lo que no cuadra.

| Pasada | Candidatos iniciales |
|:--|:--------------------|
| S1 | Las cuatro pistas que el transcript pedía verificar (Vasubandhu, Mohistas, Ibn Sīnā, Nāgārjuna) y las añadidas después en el transcript (Liu Hui, Schemmel–Boltz, Kochen–Specker, Aquinas, Scotus). |
| S2 | Aristóteles VI (contacto y continuo); Zenón/Simplicio (magnitud); Epicuro y los *minima*; el punto mohista; debate atómico Nyāya–Vaiśeṣika; otro pasaje de Vasubandhu anterior a la *Viṃśatikā*; *kalām* y tiempo discreto; al-Rāzī y contacto geométrico; la rueda pseudoaristotélica; Arquímedes y las secciones pesadas; Zu Geng; Galileo/Cavalieri; Proclo y la línea como flujo de un punto. Amplía el conjunto del transcript (Vasubandhu, Mohistas, Ibn Sīnā, Nāgārjuna, Liu Hui). |
| S3 | Jainismo, Vaiśeṣika, epistemología budista, escolástica inglesa poco citada, geometría persa, astronomía sánscrita, *wasan* japonés. Propuesta previa de S2: Jainismo, atomistas islámicos menos conocidos, escolásticos latinos, matemáticas sánscritas, Corea/Japón, fuentes persas. |
| S4 | Zenón/Simplicio; Aristóteles *Physics* VI y *De generatione et corruptione*; Ps.-Aristóteles *Mechanica* y *De lineis insecabilibus*; Epicuro; Arquímedes; *Mohist Canon* y *Zhuangzi*; Liu Hui y Zu Geng; Nāgārjuna; Nyāya–Vaiśeṣika; *Tattvārthasūtra*; Vasubandhu; Dignāga; *tathāgatagarbha* y Prajñāpāramitā; Proclo; al-Naẓẓām; Thābit; Ibn Sīnā; Khayyām; al-Qūhī/al-Sijzī; Abū al-Barakāt; Maimónides; al-Rāzī; Ṭūsī; Bhāskara II; Scotus, Harclay, Chatton, Wodeham, Heytesbury; Galileo, Cavalieri; Takebe; Corea: Choe Seok-jeong, Hong Dae-yong, Choe Han-gi. |

Cambios del mapa tras la comprobación (S4): (1) varios de los paralelos más fuertes no son atomistas: Thābit es estática; Arquímedes/Zu Geng/Cavalieri, determinación global por secciones; Dignāga, epistemología de la representación; Ṭūsī, descomposición cinemática. (2) Algunas entradas son reales pero quedan por debajo del estándar «pinpoint primario + edición crítica» (Abū al-Barakāt, al-Qūhī/al-Sijzī, Bhāskara, Takebe) frente a Aristóteles, Mohistas, Vasubandhu, Nyāya, al-Rāzī o Ṭūsī. (3) La búsqueda negativa *Heart Sūtra*–TTC 14–Aristóteles es informativa: comparabilidad sin transmisión demostrada.

## 8.2 Candidatos no promovidos

| Candidato | Motivo | Origen |
|:----------|:----------------|:--|
| Philoponus, al-Bāqillānī, al-Juwaynī | Literatura secundaria los conecta con estos debates, pero no se obtuvo pasaje primario tan preciso como los de al-Rāzī/Maimónides; quedan como búsquedas siguientes. | S2 |
| Corea (en S3), Choe Han-gi, pistas de mecánica de Thābit | Material histórico real sin pasaje tan preciso como los promovidos en S3. S4 los incorpora después con los estados indicados en E31, E54, E55. | S3 |
| Choe Seok-jeong, *Gusuryak* | Ajuste temático débil (E51). | S4 |
| Hong Jeong-ha | Analogía lateral (E52). | S5 |

## 8.3 Siguiente ronda propuesta (S3)

Tíbet (Dharmakīrti y comentaristas); Armenia/Georgia y Bizancio tardío; ismāʿīlíes (*Ismāʿīlīes*); matemáticos hebreos medievales; problemas de «contacto sin penetración» en óptica/perspectiva. Motivo: Dignāga y Takebe sugieren que buscar solo bajo *continuum/atomism* deja fuera material pertinente.

## 8.4 Pins y ediciones pendientes (consolidado)

| Entrada | Pendiente |
|:--|:------------------------|
| E09 Arquímedes | Pin crítico (Heiberg/Heath o Netz). |
| E13 *De lineis insecabilibus* | Edición y locus. |
| E15 Nyāya *avayavin* | Pin primario (solo vía IEP). |
| E16 Vaiśeṣika | Pin primario (solo vía SEP). |
| E19/E20 Liu Hui | Edición crítica junto al facsímil. |
| E23 AKBh I.43d | Texto sánscrito crítico del AKBh. |
| E25 Proclo | Pin Friedlein desde facsímil. |
| E26 Zu Geng | Facsímil o edición Chemla–Guo. |
| E27 Dignāga | Edición crítica estable. |
| E29 Woncheuk | Número Taishō y folio (CBETA/SAT). |
| E30 al-Naẓẓām | Edición árabe y traducción académica posterior a Haarbrücker. |
| E32 al-Qūhī/al-Sijzī | Texto árabe con folio/página. |
| E37 Khayyām | Pin árabe crítico. |
| E38 Abū al-Barakāt | Edición árabe con volumen/página. |
| E39 Bhāskara II | Estrofa sánscrita críticamente fijada. |
| E41 al-Rāzī | Texto árabe crítico + traducción de VI.48–49 (y VI.52, VI.71). |
| E45 Harclay | *Quaestio*/página. |
| E46 Chatton | Edición primaria y pin. |
| E48 Heytesbury | Folio de la formulación contrafactual. |
| E49 Cavalieri | Edición digital primaria. |
| E50 Galileo | Facsímil 1638 o Edizione Nazionale. |
| E53 Takebe | Página de edición japonesa. |
| E54 Hong Dae-yong | Pin de línea en el original. |
| E55 Choe Han-gi | Lectura de las treinta unidades de `推動測靜`. |
| E56 Choe Han-gi | Pins primarios. |
| E58 RGV | Texto sánscrito crítico. |

# 9. Registro de discrepancias entre fuentes

| Nº | Tema | Versiones | Tratamiento aquí |
|:--|:------|:----------------|:----------|
| D01 | Fecha de TTC 14 | S4: s. IV–III a. C. · S5: c. s. VI–V a. C. | Ambas en E02. |
| D02 | Locus de Aristóteles sobre Leucipo/Demócrito | S4: *GC* I.8–9 (≈325a) · S5: *Metaph.* I.4 | Complementarios; ambos en E04. |
| D03 | Rango de la *Viṃśatikā* | S1, S5: vv. 11–13 · S4: vv. 11–15 | Ambos; v. 12 común. |
| D04 | Fecha de Vasubandhu | S4: s. IV–V · S5: s. V (*Viṃśatikā*), s. IV–V (AKBh) | E23, E24. |
| D05 | Fecha de Dignāga | S4: c. 480–540 · S5: s. V | E27. |
| D06 | Fecha de Epicuro | S4: c. 300 a. C. · S5: s. III a. C. | E10. |
| D07 | Fecha de Nāgārjuna | S4: c. 150–250 · S5: c. s. II–III | E18. |
| D08 | *Tattvārthasūtra* | Fecha S4: c. s. II–V · S5: c. s. I–V. Regla de *bandha*: 5.32 o 5.33 según recensión. | E21; guardar *incipit*. |
| D09 | Scotus, números | S1: nn. 289–292 · S4: nn. 287–292, rango 284–376 | E44. |
| D10 | al-Rāzī, páginas | S2: VI 48–49 y 52 · S4: VI 48–49 y 71 | Complementarios; E41. |
| D11 | Thābit | S4: estática/equilibrio/medición, confirmado, prioridad A · S5: mereología atomista `UNSPECIFIED`, rama geométrica/neoarquimediana · S3: no promovido | Coinciden en «no atomismo»; difieren en la clasificación. Ambas en E31. |
| D12 | Choe Han-gi, `推動測靜` | S4: tesis técnica no confirmada · S5: afirma que la sección articula inferencia de lo estático desde lo móvil, sin pasaje citado · S3: no promovido | Estado operativo de S4 (target; pasaje pendiente). |
| D13 | Definición de H10/H11 | S4: primario / interpretativo · S5: estático / dinámico | §7.1; ambas asignaciones en §2. |
| D14 | Traducción de B17 | S1 (Schemmel–Boltz): «re-cast» · S5-EN: «re-formed» · S5-ES: «rehecha/reformada» | Prevalece la de la edición (S1). |
| D15 | Choe Seok-jeong, vida | S5: «1664–?». Nota del editor (memoria, no verificada en esta fusión): suele darse 1646–1715. | Verificar antes de usar. |
| D16 | Fecha Schemmel–Boltz | Archivo local 2023 · © 2022 | Resuelto: 2022 (E07). |
| D17 | Fecha Kochen–Specker | 1967 (convencional) · 1968 (DOI) | Ambas (E57). |
| D18 | Vives de Scotus | Archivo local «1891» · tomo XI = 1893 | Resuelto (E44). |
| D19 | Variantes ES/EN de S5 | EN: «emptiness of the five skandhas»; ES: «vacuidad de los dharmas». Orden de las citas chinas del *Heart Sūtra* distinto. EN califica de «geometrical» los argumentos de Scotus. ES lista una fuente más (De Gruyter, Rashed). | Todas conservadas (E28, E32, E44). |
| D20 | Contenido anunciado de S5 | El chat anuncia tres columnas de relevancia, tablas de atribuciones problemáticas y diagramas Mermaid; ausentes en los archivos. | No recuperable. |
| D21 | Zenón, loci | S4: 139.7–15; 141.1 ss. · S2: 139.9 y 141.2, DK B1 | Complementarios; E01. |
| D22 | Número de familias de problemas | S4: cinco · S5: cuatro | §1.1. |
| D23 | al-Naẓẓām, ejemplos | S5: hormiga, cuerda/pozo · S4: rueda/piedra de molino | Complementarios; E30. |
| D24 | URLs de GRETIL y Wikisource | S1 y S4 usan URL distintas para Nāgārjuna, *Viṃśatikā* y *Zhuangzi* | Todas conservadas. |
| D25 | Fecha de *Zhuangzi* 33 | S4: s. III–II a. C. · S5: s. III a. C. | E11. |
| D26 | Heytesbury | S3, S5 enuncian la definición contrafactual como contenido · S4 exige folio antes de citarla entre comillas | E48: contenido registrado, cita pendiente. |


# Anexo A. Registro de URL

Todos los URL externos de S1–S5, deduplicados. Formas sin `utm_source=chatgpt.com`. Variantes del mismo recurso con URL distinto se listan por separado. «Aparece en»: página del PDF (S1–S3 = páginas de la exportación del chat; S4-pdf = páginas de `Investigacio_n_avanzada.pdf`) o archivo `.md`. Excluidos por no ser referencias: enlaces internos de chatgpt.com y del visor de informes (ver `aux_trazabilidad.md` §2).

| Nº | URL | Entradas | Aparece en |
|:--|:----------------------|:----|:--------|
| U01 | <https://seop.illc.uva.nl//archives/fall2015/entries/paradox-zeno/> | E01 | S2 p. 4 |
| U02 | <https://seop.illc.uva.nl/entries/zeno-elea/> | E01 | S4-pdf p. 3,29 |
| U03 | <https://daodejing.ru/fr/chapters/14> | E02 | S4-md; S4-pdf p. 3 |
| U04 | <https://www.tao-te-ching.org/14> | E02 | S4-md; S4-pdf p. 3,19,20,21,29 |
| U05 | <https://classics.mit.edu/Aristotle/physics.6.vi.html> | E03 | S5-ES; S5-EN |
| U06 | <https://www.logicmuseum.com/wiki/Authors/Aristotle/physics/liber6> | E03 | S2 p. 4,6 |
| U07 | <https://www.logoslibrary.org/aristotle/physics/601.html> | E03 | S4-md; S4-pdf p. 1,3,21,22,26,28,29 |
| U08 | <https://catalog.perseus.org/catalog/urn%3Acts%3AgreekLit%3Atlg0086.tlg013.opp-grc1> | E04 | S4-md; S4-pdf p. 4,29 |
| U09 | <https://classics.mit.edu/Aristotle/gener_corr.html> | E04 | S4-md; S4-pdf p. 4 |
| U10 | <https://en.wikisource.org/wiki/Page:Metaphysics_by_Aristotle_Ross_1908_(deannotated).djvu/31> | E04 | S5-ES; S5-EN |
| U11 | <https://www.ellopos.net/elpenor/greek-texts/ancient-greece/aristotle/generation-corruption.asp> | E04 | S4-pdf p. 21,26,31 |
| U12 | <https://doi.org/10.1007/978-3-031-08797-4> | E05, E07 | S4-md; S4-pdf p. 4 |
| U13 | <https://link.springer.com/book/10.1007/978-3-031-08797-4> | E05, E07 | S1 p. 1; S4-pdf p. 2,4,24,25,26,29 |
| U14 | <https://link.springer.com/chapter/10.1007/978-3-031-08797-4_2> | E05 | S2 p. 4,6; S4-pdf p. 22,31 |
| U15 | <https://www.mprl-series.mpg.de/studies/8/5/index.html> | E05 | S2 p. 4 |
| U16 | <https://upload.wikimedia.org/wikipedia/commons/6/6f/Matthias_Schemel_and_William_G._Boltz_-_Theoretical_Knowledge_in_the_Mohist_Canon.pdf> | E06, E07, E08 | S1 p. 1,3 |
| U17 | <https://old.maa.org/> | E09 | S5-ES; S5-EN |
| U18 | <https://old.maa.org/press/periodicals/convergence/archimedes-method-for-computing-areas-and-volumes-proposition-2-of-the-method?device=mobile> | E09 | S2 p. 5,7 |
| U19 | <https://ericlyonshansen.github.io/Epicurus/Letter_to_Herodotus_Bailey.html> | E10 | S4-md; S4-pdf p. 5 |
| U20 | <https://ericlyonshansen.github.io/Epicurus/Letter_to_Herodotus_Bailey_Lines.html> | E10 | S2 p. 4 |
| U21 | <https://societyofepicurus.com/epicurus-epistle-to-herodotus/> | E10 | S4-pdf p. 5,29 |
| U22 | <https://zh.wikisource.org/wiki/%E8%8E%8A%E5%AD%90/%E5%A4%A9%E4%B8%8B> | E11 | S1 p. 1 |
| U23 | <https://zh.wikisource.org/zh-hant/%E8%8E%8A%E5%AD%90/%E5%A4%A9%E4%B8%8B> | E11 | S4-md; S4-pdf p. 5,22,29 |
| U24 | <https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Aristotle/Mechanica%2A.html> | E12 | S2 p. 5; S4-md; S4-pdf p. 5,29 |
| U25 | <https://cl.sanskrit.du.ac.in/etexts/etext.php?text=nyayasutra> | E14 | S2 p. 4; S4-md; S4-pdf p. 6,26,29 |
| U26 | <https://iep.utm.edu/nyaya/> | E15 | S2 p. 5 |
| U27 | <https://plato.stanford.edu/entries/naturalism-india/> | E16 | S3 p. 8 |
| U28 | <https://en.wikipedia.org/wiki/The_Nine_Chapters_on_the_Mathematical_Art> | E17 | S4-pdf p. 6,29 |
| U29 | <https://liucan.me/projects/chinese-calculus/> | E17, E19, E26 | S4-pdf p. 7,9,22,24,26,29 |
| U30 | <https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/6_sastra/3_phil/buddh/nagmmk_u.htm> | E18 | S1 p. 2 |
| U31 | <https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/html/sa_nAgArjuna-mUlamadhyamakakArikA.htm> | E18 | S4-md; S4-pdf p. 6,29 |
| U32 | <https://zh.wikisource.org/zh-hant/%E5%8A%89%E5%BE%BD%E5%89%B2%E5%9C%93%E8%A1%93> | E19 | S1 p. 2; S4-md; S4-pdf p. 7 |
| U33 | <https://zh.wikisource.org/wiki/Page%3ASibu_Congkan0391-%E5%8A%89%E5%BE%BD-%E4%B9%9D%E7%AB%A0%E7%AE%97%E8%A1%93-3-2.djvu/18> | E20 | S1 p. 2 |
| U34 | <https://zh.wikisource.org/wiki/Page%3ASibu_Congkan0391-%E5%8A%89%E5%BE%BD-%E4%B9%9D%E7%AB%A0%E7%AE%97%E8%A1%93-3-2.djvu/19> | E20 | S1 p. 2 |
| U35 | <https://www.wisdomlib.org/jainism/book/tattvartha-sutra-with-commentary/d/doc1084760.html> | E21 | S3 p. 8 |
| U36 | <https://www.wisdomlib.org/jainism/book/tattvartha-sutra-with-commentary/d/doc1084765.html> | E21 | S3 p. 8,11; S4-pdf p. 7,29 |
| U37 | <https://www.wisdomlib.org/jainism/book/tattvartha-sutra-with-commentary/d/doc1084768.html> | E21 | S3 p. 10; S4-pdf p. 24,26,31 |
| U38 | <https://www.wisdomlib.org/jainism/book/tattvartha-sutra-with-commentary/d/doc1084787.html> | E21 | S3 p. 8; S4-pdf p. 25,31 |
| U39 | <https://buddhanature.tsadra.org/index.php/Tath%C4%81gata_Essence_S%C5%ABtra> | E22 | S4-md; S4-pdf p. 7,20,29 |
| U40 | <https://wstb.univie.ac.at/wp-content/uploads/WSTB_94.pdf> | E23 | S2 p. 4,6 |
| U41 | <https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/6_sastra/3_phil/buddh/vasvvmsu.htm> | E24 | S4-md; S4-pdf p. 8,26,29 |
| U42 | <https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/html/sa_vasubandhu-viMzatikA-vijJaptimAtratAsiddhi.htm> | E24 | S1 p. 1 |
| U43 | <https://www.cambridge.org/core/books/conceptualising-concepts-in-greek-philosophy/concepts-in-greek-mathematics/DC34401AA94103E01D51253EACB2C92D> | E25 | S2 p. 5,6; S4-pdf p. 8,29 |
| U44 | <https://donwagner.dk/SPHERE/SPHERE.html> | E26 | S2 p. 6,7 |
| U45 | <https://journals.ub.uni-heidelberg.de/index.php/jiabs/article/download/8988/2881/8782> | E27 | S3 p. 8 |
| U46 | <https://plato.stanford.edu/entries/yogacara/> | E27 | S3 p. 10 |
| U47 | <https://84000.co/translation/toh531.pdf> | E28 | S4-pdf p. 9,20,21,23,27,29 |
| U48 | <https://en.wikipedia.org/wiki/Heart_Sutra> | E28, E29 | S4-pdf p. 10,19,30 |
| U49 | <https://journals.ub.uni-heidelberg.de/index.php/jiabs/article/view/8800> | E28 | S5-ES; S5-EN |
| U50 | <https://reader.84000.co/entity/passage/4d1896b2-dcf3-4b01-8cc6-8bd5e30c9d67> | E28 | S4-md; S4-pdf p. 9 |
| U51 | <https://opendata.uni-halle.de/bitstream/1981185920/47211/2/407352872.pdf> | E30 | S1 p. 3 |
| U52 | <https://www.deutsche-digitale-bibliothek.de/item/36IDSI3RR6PD2TOYCV6GYZLQF533HUK2> | E30 | S1 p. 3 |
| U53 | <https://al-furqan.com/the-corpus-of-the-arabic-science-of-weights-9th-19th-centuries-codicology-textual-tradition-and-theoretical-scope/?ver=2.0.3> | E31 | S4-pdf p. 10,18,24,25,27,30 |
| U54 | <https://en.wikipedia.org/wiki/Th%C4%81bit_ibn_Qurra> | E31 | S4-pdf p. 18,30 |
| U55 | <https://www.cambridge.org/core/journals/arabic-sciences-and-philosophy/article/abs/alquhi-and-alsijzi-on-the-perfect-compass-and-the-continuous-drawing-of-conic-sections/9C08F654631883D4CDFF486D23437A18> | E32 | S3 p. 9 |
| U56 | <https://www.degruyter.com/> | E32 | S5-ES |
| U57 | <https://press.uchicago.edu/ucp/books/book/distributed/P/bo10581412.html> | E33, E34, E36 | S1 p. 2; S4-md; S4-pdf p. 11 |
| U58 | <https://www.mercaba.es/islam/fisica_de_avicena.pdf> | E33, E34 | S1 p. 2 |
| U59 | <https://academic.oup.com/book/3244> | E35 | S1 p. 2 |
| U60 | <https://plato.stanford.edu/entries/umar-khayyam/index.html> | E37 | S3 p. 10 |
| U61 | <https://www.iranicaonline.org/articles/khayyam-omar/khayyam-omar-xiv-as-mathematician/> | E37 | S3 p. 9 |
| U62 | <https://www.cambridge.org/core/journals/arabic-sciences-and-philosophy/article/reception-of-avicennas-theory-of-motion-in-the-twelfth-century/85EF5D5AEDC78A6459C920B02945B39A> | E38 | S3 p. 9 |
| U63 | <https://iks.iitgn.ac.in/wp-content/uploads/2016/02/Indian-Tradition-of-Science-an-Introductory-Overview-MD-Srinivas-Feb-2016.pdf> | E39 | S3 p. 9 |
| U64 | <https://www.sefaria.org/Guide_for_the_Perplexed%2C_Part_1.73> | E40 | S2 p. 5; S4-md; S4-pdf p. 12,30 |
| U65 | <https://jisarchive.cis-ca.org/_media/pdf/2006/2/A_avhitkoaaaapstma.pdf> | E41 | S2 p. 6 |
| U66 | <https://plato.sydney.edu.au/entries/al-din-al-razi/> | E41 | S2 p. 5,7; S4-md; S4-pdf p. 12,27,30 |
| U67 | <https://www.corpusthomisticum.org/scg3064.html> | E42 | S1 p. 3 |
| U68 | <https://www.liriocatolico.com.br/suma_contra_gentios/view/SCG3.C77/> | E42 | S4-pdf p. 13,25,30 |
| U69 | <https://wellcomecollection.org/works/s6gufpfm> | E43 | S4-pdf p. 13,27,30 |
| U70 | <https://www.davidboeno.org/GROEUVRE/CONIQUES/tusiII11.html> | E43 | S4-pdf p. 24,31 |
| U71 | <https://www.iranicaonline.org/articles/tusi-nasir-al-din-mathematician-astronomer/> | E43 | S3 p. 9 |
| U72 | <https://openlibrary.org/works/OL15847667W/Opera_omnia> | E44 | S1 p. 3 |
| U73 | <https://www.logicmuseum.com/wiki/Authors/Duns_Scotus/Ordinatio/Ordinatio_II/D2/P2Q5> | E44 | S1 p. 3; S4-md; S4-pdf p. 13,25,27,30; S5-ES; S5-EN |
| U74 | <https://journals.uco.es/refime/article/view/14564> | E45 | S4-pdf p. 14,30 |
| U75 | <https://plato.stanford.edu/archives/sum2010/entries/walter-chatton/> | E45, E46 | S3 p. 8 |
| U76 | <https://plato.stanford.edu/entries/walter-chatton/> | E45, E46 | S5-ES; S5-EN |
| U77 | <https://link.springer.com/book/10.1007/978-94-009-1425-4> | E47 | S3 p. 9 |
| U78 | <https://www.cambridge.org/core/journals/british-journal-for-the-history-of-science/article/abs/adam-de-wodeham-tractatus-de-indivisibilibus-a-critical-edition-introduction-translation-and-textual-notes-by-rega-wood-synthese-historical-library-volume-31-dordrecht-boston-london-kluwer-academic-publishers-1988-pp-vii-333-isbn-9027724245-7400/892EB67EFB311772A40BD5C5611BEDFA> | E47 | S4-pdf p. 14,27,30 |
| U79 | <https://bibnum.publimath.fr/ACF/ACF08001.pdf> | E48 | S3 p. 9 |
| U80 | <https://gredos.usal.es/handle/10366/84387> | E48 | S4-md; S4-pdf p. 15 |
| U81 | <https://plato.stanford.edu/entries/heytesbury/> | E48 | S4-md; S4-pdf p. 15,30 |
| U82 | <https://plato.stanford.edu/entries/continuity/> | E49 | S5-ES; S5-EN |
| U83 | <https://plato.stanford.edu/entries/continuity/index.html> | E49 | S2 p. 6,7 |
| U84 | <https://falsafa.ai/works/galileo-galilei-dialogues-concerning-two-new-sci-8eceb2/05-two-new-sciences-by-galileo-first-day-interlocutor/translation/> | E50 | S2 p. 5,6 |
| U85 | <https://en.wikipedia.org/wiki/Choi_Seok-jeong> | E51 | S4-pdf p. 16,30 |
| U86 | <https://mathsci.kaist.ac.kr/home/en/2018/09/opening-of-choi-seok-jeong-seminar-room/> | E51 | S4-pdf p. 19,31 |
| U87 | <https://mathshistory.st-andrews.ac.uk/Biographies/Takebe/> | E53 | S3 p. 9,11 |
| U88 | <https://klwave.or.kr/klw/directories/200300/authorsView.do> | E54 | S4-pdf p. 1,16,18,29 |
| U89 | <https://openlibrary.org/works/OL33545816W/Imha_ky%C5%8Fngnyun_%C5%ACisan_mundap> | E54 | S4-pdf p. 19,28,30 |
| U90 | <https://books.google.com/books/about/%E7%A5%9E%E6%B0%A3%E9%80%9A_%E6%8E%A8%E6%B8%AC%E9%8C%84_%E7%BF%92%E7%AE%97%E6%B4%A5%E7%AD%8F.html?id=bGY_zgEACAAJ> | E55 | S4-pdf p. 17,28,30 |
| U91 | <https://en.wikipedia.org/wiki/Choe_Han-gi> | E55, E56 | S4-pdf p. 17,30 |
| U92 | <https://encykorea.aks.ac.kr/Article/E0057904> | E55 | S5-ES; S5-EN |
| U93 | <https://www.namu.moe/w/%EA%B8%B0%EC%B8%A1%EC%B2%B4%EC%9D%98> | E55 | S4-pdf p. 19,30 |
| U94 | <https://cds.cern.ch/record/429520> | E57 | S1 p. 3 |
| U95 | <https://doi.org/10.1512/iumj.1968.17.17004> | E57 | S1 p. 3 |
| U96 | <https://buddhanature.tsadra.org/index.php/Texts/Ratnagotravibh%C4%81ga_Mah%C4%81y%C4%81nottaratantra%C5%9B%C4%81stra/English> | E58 | S4-pdf p. 2,20,21,23,27,29 |
| U97 | <https://buddhanature.tsadra.org/index.php/Articles/All_Buddhas_and_All_Living_Beings_Are_Just_This_One_Mind> | E59 | S4-pdf p. 20,31 |

# Anexo B. Identificadores, manuscritos y ediciones citados

## B.1 DOI, ISBN, manuscritos y signaturas

| Tipo | Identificador | Obra | Entrada |
|:--|:----------------|:----------------|:--|
| DOI | 10.1007/978-3-031-08797-4 | Schemmel & Boltz, *Theoretical Knowledge in the Mohist Canon*, Archimedes 63 | E07 |
| DOI | 10.1093/acprof:oso/9780195331479.001.0001 | McGinnis, *Avicenna* | E35 |
| DOI | 10.1017/S0269889701000084 | Abattouy, *Science in Context* 14 (2001) | E31 |
| DOI | 10.21071/refime.v29i2.14564 | Crialesi, REFIME | E45 |
| DOI | 10.1512/iumj.1968.17.17004 | Kochen & Specker, *J. Math. Mech.* 17 | E57 |
| DOI (URL Springer) | 10.1007/978-94-009-1425-4 | Wood, *Adam de Wodeham: Tractatus de Indivisibilibus* | E47 |
| ISBN | 978-0-19-533147-9 | McGinnis, *Avicenna*, OUP 2010 | E35 |
| ISBN | 978-0-8425-2747-7 | Avicenna, *The Physics of The Healing*, BYU 2009 | E36 |
| ISBN | 90-277-2424-5 | Wood 1988, Kluwer | E47 |
| Manuscrito | British Library, India Office Islamic 461, ff. 198v–207r (copia de 1198; Qatar Digital Library) | Thābit, *Kitāb fī l-qarasṭūn* | E31 |
| Manuscrito | Princeton, Garrett 4045Y | al-Shahrastānī, *al-Milal wa-l-niḥal* | E30 |
| Canon budista | Toh 531; T251 | *Heart Sūtra* | E28 |
| Canon budista | T666, T667; D258/Q924 | *Tathāgatagarbha Sūtra* | E22 |
| Serie | Archimedes 63 (Springer) | Schemmel & Boltz | E07 |
| Serie | Synthese Historical Library 31 (Kluwer) | Wood 1988 | E47 |
| Serie | CAG IX | Diels, Simplicio | E01 |

## B.2 Ediciones, traducciones y estudios mencionados

| Autor / editor | Datos | Entrada |
|:----------|:----------------------|:--|
| H. Diels | *Simplicii in Aristotelis Physicorum libros commentaria*, CAG IX, Berlín, 1882 | E01 |
| I. Bekker | Texto griego de *De generatione et corruptione*, 1831 (catálogo Perseus); números Bekker de *Physics* | E03, E04 |
| Hardie–Gaye | Traducción de *Physics* | E03 |
| H. H. Joachim | Traducción de *De generatione et corruptione* | E04 |
| W. D. Ross | *Metaphysics*, 1908 | E04 |
| M. Schemmel & W. G. Boltz | 2022 (E07) | E05–E08 |
| A. C. Graham; N. Sivin; J. Needham, S. Nakayama; W. G. Boltz; Yang Bojun; Dai Nianzu | Ver E08 | E08 |
| J. L. Heiberg / T. L. Heath; R. Netz | Ediciones del *Method* recomendadas | E09 |
| C. Bailey | *Epicurus: The Extant Remains*, 1926 | E10 |
| S. Lévi; Hakuju Ui | Edición de la *Viṃśatikā*, 1925; correcciones, 1953 (base de GRETIL) | E24 |
| G. Friedlein | *Procli Diadochi in primum Euclidis Elementorum librum commentarii*, Leipzig, 1873 | E25 |
| D. B. Wagner | Traducción y reconstrucción de la demostración de Zu Geng | E26 |
| K. Chemla – Guo Shuchun | Edición recomendada de *Nine Chapters* | E26 |
| Li Chunfeng | Transmisor de la frase de Zu Geng | E26 |
| M. Zimmermann | *A Buddha Within*, 2002 | E22 |
| J. Nattier | Estudio del *Heart Sūtra*, JIABS, 1992 | E28 |
| 84000 | Traducción de Toh 531 | E28 |
| Kuiji | Comentario temprano al *Heart Sūtra* | E29 |
| T. Haarbrücker | *Abu-'l-Fath Muh'hammad asch-Schahrastâni's Religionspartheien und Philosophen-Schulen*, I, Halle: Schwetschke, 1850 | E30 |
| M. Abattouy | «Greek Mechanics in Arabic Context: Thābit ibn Qurra, al-Isfizārī and the Arabic Traditions of Aristotelian and Euclidean Mechanics», 2001 | E31 |
| R. Rashed | Historia de la matemática árabe (compás perfecto) | E32 |
| J. McGinnis | *Avicenna*, OUP 2010; *The Physics of The Healing*, BYU 2009 | E33–E36 |
| Ibn al-Haytham | Criticado por Khayyām por introducir movimiento | E37 |
| M. Friedländer | Traducción inglesa de la *Guía* | E40 |
| Enrique Alarcón | Texto leonino revisado (Corpus Thomisticum) | E42 |
| F. J. Ragep | *Naṣīr al-Dīn al-Ṭūsī's Memoir on Astronomy*, 2 vols., Springer, 1993 | E43 |
| L. Vivès | Scotus, *Opera omnia*, París, 1891–95; t. XI, 1893 | E44 |
| M. G. Henninger; R. Edwards | *Henry of Harclay: Ordinary Questions*, OUP, 2008 | E45 |
| Crialesi | REFIME, recepción latina de *De lineis indivisibilibus* | E45 |
| R. Wood | *Tractatus de Indivisibilibus*, 1988 | E47 |
| — | Heytesbury, *Regulae*, incunable Venecia 1491 (Univ. Salamanca) | E48 |
| B. Cavalieri | *Geometria indivisibilibus…*, 1635 | E49 |
| — | Galileo, *Discorsi*, Leiden: Elsevier, 1638; Edizione Nazionale | E50 |
| Kyujanggak Institute for Korean Studies | Custodia de *Gusuryak* | E51 |
| Konkuk University Press | *Imha kyŏngnyun, Ŭisan mundap*, 1975; *Damhŏnsŏ* (facsímil sugerido) | E54 |
| Sungkyunkwan University Daedong Institute | *神氣通, 推測錄, 習算津筏*, 1971 | E55 |
| Pūjyapāda | *Sarvārthasiddhi* | E21 |

