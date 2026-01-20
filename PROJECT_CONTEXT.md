# CONTEXTO DEL PROYECTO - Biochar Insights Dashboard

> **Última actualización:** 2026-01-20
> **Cliente:** Libertario Coffee
> **Repositorio:** https://github.com/Fsardi19/biochar-dashboard

---

## 1. RESUMEN EJECUTIVO

Dashboard de análisis de encuesta sobre el **Proyecto Biochar** de Libertario Coffee, donde se destina el **3% de las ventas** a financiar biochar en fincas cafeteras.

### KPIs Principales
| Métrica | Valor |
|---------|-------|
| Total encuestados válidos | **836** |
| Excluidos (Omitidas) | 2 |
| Conocía la iniciativa | **22%** |
| Me encanta + Me gusta | **91%** |
| Influye en retorno (bastante/decisivo) | **43.7%** |

### Período de datos
- **Inicio:** 2025-11-11
- **Fin:** 2026-01-07

---

## 2. ESTRUCTURA DE DATOS

### Archivo fuente original
```
/Users/felipesardi/Downloads/datos_crudos_encuesta_20250108.csv
```
- Formato "largo" (cada respuesta es una fila)
- 15,566 filas totales
- 838 encuestados únicos (por timestamp)

### Archivos procesados
```
/Users/felipesardi/Downloads/output/
├── encuestados_pivoteado.json    # Datos transformados (836 válidos)
└── metricas_biochar.json         # Métricas calculadas

/Users/felipesardi/Downloads/biochar-dashboard/data/
├── metricas_biochar.json         # Copia para el dashboard
└── metricas_por_tienda.json      # Métricas detalladas por tienda
```

### Scripts de procesamiento
```
/Users/felipesardi/Downloads/
├── transform_encuesta.py         # Transforma CSV largo → JSON ancho
└── calcular_metricas.py          # Calcula métricas generales
└── calcular_metricas_tienda.py   # Calcula métricas por tienda
```

---

## 3. DISTRIBUCIÓN GEOGRÁFICA

### Por País
| País | Encuestados | % |
|------|-------------|---|
| Colombia (CO) | 438 | 52.4% |
| Sin especificar | 330 | 39.5% |
| Costa Rica (CR) | 42 | 5.0% |
| México (MX) | 26 | 3.1% |

### Por Coffee Shop (12 tiendas)
| Tienda | n | Satisfacción | Influye Retorno | Top Beneficio |
|--------|---|--------------|-----------------|---------------|
| CO - Getsemani | 7 | 100.0% | 71.4% | Biodiversidad del suelo |
| MX - Colima 340 | 11 | 100.0% | 63.6% | Orgullo de consumo |
| CO - FIC48 | 46 | 97.8% | 45.7% | Mejor sabor en taza |
| CO - Calle 85 | 47 | 95.7% | 80.9% | Menos químicos |
| CO - Usaquen | 45 | 95.6% | 62.2% | Más nutrientes |
| MX - Roma Norte | 15 | 93.3% | 80.0% | Más ingresos caficultores |
| CO - 122 B | 39 | 92.3% | 43.6% | Menos basura en finca |
| CO - Calle 109 | 83 | 91.6% | 43.4% | Menos basura en finca |
| CO - Zona G | 59 | 91.5% | 44.1% | Menos químicos |
| CO - Calle 79 | 35 | 91.4% | 77.1% | Orgullo de consumo |
| CO - Calle 93 | 77 | 87.0% | 45.5% | Mejor sabor en taza |
| **CR - Escalante** | 42 | **71.4%** ⚠️ | 42.9% | Conexión productor |

---

## 4. RANKING DE BENEFICIOS BIOCHAR

Los 13 beneficios evaluados (escala 1-5):

| # | Beneficio | Promedio | % Promotores (4-5) |
|---|-----------|----------|-------------------|
| 1 | Menos químicos | 4.51 | 89.2% |
| 2 | Menos basura en finca | 4.47 | 87.6% |
| 3 | Mayor biodiversidad del suelo | 4.47 | 88.2% |
| 4 | Mayor resiliencia climática | 4.47 | 87.9% |
| 5 | Más nutrientes disponibles | 4.46 | 86.6% |
| 6 | Suelos más sanos y productivos | 4.44 | - |
| 7 | Menos erosión | 4.41 | - |
| 8 | Mayor retención de agua | 4.40 | - |
| 9 | Captura de CO₂ estable | 4.37 | - |
| 10 | Orgullo de consumo responsable | 4.35 | - |
| 11 | Conexión productor-consumidor | 4.32 | - |
| 12 | Más ingresos para caficultores | 4.17 | - |
| 13 | Mejor sabor en taza | 3.93 | - |

---

## 5. ALERTAS Y PRIORIDADES

### 🚨 ALERTA: CR - Escalante
- Satisfacción: **71.4%** (vs 91% promedio)
- 28.6% dice "Me gusta poco" o "No me gusta"
- 31% dice que "No influye" en retorno
- **Acción:** Investigar con equipo local

### ⚠️ ATENCIÓN: CO - Calle 93
- Bajo awareness (19.5%)
- 13% insatisfechos
- Pero 88.3% son recurrentes
- **Acción:** Campaña de educación

### 🌟 MODELO: CO - Calle 85
- 95.7% satisfacción
- 80.9% dice que influye en retorno
- 46.8% primera vez (mercado en expansión)
- **Acción:** Documentar mejores prácticas

---

## 6. MENSAJES SUGERIDOS POR TIENDA

Cada tienda tiene un mensaje personalizado basado en:
- Su beneficio #1
- Perfil de clientes (primera vez vs recurrentes)
- Nivel de satisfacción

Ejemplos:
- **CO - Calle 85:** "¿Primera vez en Libertario? Aquí tu café tiene impacto: apoyamos menos químicos con el 3% de cada venta."
- **MX - Roma Norte:** "Tu café de hoy = más ingresos caficultores. El 3% de esta compra financia biochar en fincas."
- **CR - Escalante:** "En Escalante, cada taza apoya a caficultores. Pregúntanos cómo funciona." (educativo)

---

## 7. ESTRUCTURA DEL DASHBOARD

### Repositorio
```
biochar-dashboard/
├── app.py                    # Aplicación Streamlit principal
├── requirements.txt          # streamlit>=1.28.0, plotly>=5.18.0
├── README.md                 # Documentación
├── PROJECT_CONTEXT.md        # Este archivo
├── GUIA_COMUNICACION.md      # Lineamientos de comunicación (Emilio)
├── GUIA_COMUNICACION_POR_PAIS.md  # Guía práctica por país (CO, CR, MX)
├── Guia de contenidos..docx  # Documento original Emilio
├── Guia de entrega de contenidos.docx  # Documento original Emilio
├── .gitignore
├── .streamlit/
│   └── config.toml           # Tema con colores Libertario
└── data/
    ├── metricas_biochar.json
    └── metricas_por_tienda.json
```

### Páginas del Dashboard
1. **📊 Vista Ejecutiva** - KPIs, gráfico de opinión, ranking beneficios, satisfacción por tienda
2. **🏪 Todas las Tiendas** - Grid visual, tabla comparativa
3. **🔍 Análisis por Tienda** - Selector → métricas, top/bottom beneficios, insights, recomendaciones, gráficos
4. **💬 Mensajes Sugeridos** - Mensaje personalizado para cada tienda
5. **💡 Insights** - Alertas, prioridades, recomendaciones estratégicas

### Colores de Marca
- Verde Oscuro: `#2C5530`
- Verde Claro: `#4A7C59`
- Café: `#8B4513`
- Beige: `#F5DEB3`
- Crema: `#FFF8DC`

---

## 8. DEPLOY

### GitHub
- **Repo:** https://github.com/Fsardi19/biochar-dashboard
- **Branch:** main

### Streamlit Cloud
- **URL:** [Pendiente de configurar en share.streamlit.io]
- **Main file:** `app.py`

### Local
```bash
cd "/Users/felipesardi/Desktop/EL GREEN HUB/COFFEE SHOPS/AI STRATEGY/biochar-dashboard"
pip install -r requirements.txt
streamlit run app.py
```

---

## 9. ESTRATEGIA DE COMUNICACIÓN EN TIENDAS

> **Lineamientos generales:** `GUIA_COMUNICACION.md`
> **Guía práctica por país:** `GUIA_COMUNICACION_POR_PAIS.md`

### Resumen de la Estrategia
- **Canal**: Pantallas en tiendas + códigos QR para profundizar
- **Formato**: Máximo 5 imágenes rotando cada 3 minutos
- **Regla**: Máximo 7 palabras por imagen
- **Prueba piloto**: Colombia, 1 mes

### 3 Áreas Temáticas de Mensajes
1. **Naturaleza**: Agua, Suelo, Biodiversidad, Aire
2. **Cambio Climático**: Captura de carbono
3. **Impacto Económico**: Ahorros y mayores ingresos para caficultores

### Tipos de Contenido
- **Declaraciones**: Valores y compromisos de Libertario
- **Opiniones informadas**: Basadas en evidencia, siempre con fuente citada

### Conexión con Dashboard
Los datos de la encuesta permiten personalizar mensajes por tienda según:
- Beneficio #1 de cada local
- Nivel de awareness
- Perfil de clientes (primera vez vs recurrentes)

---

## 10. PRÓXIMOS PASOS SUGERIDOS

1. [ ] Completar deploy en Streamlit Cloud
2. [ ] Investigar baja satisfacción en CR - Escalante
3. [ ] Implementar material visual en tiendas con bajo awareness
4. [ ] Programa de embajadores en tiendas con alta influencia en retorno
5. [ ] Catas comparativas en tiendas donde "sabor" es driver #1
6. [ ] Diseñar las 5 imágenes para pantallas según guía de comunicación
7. [ ] Preparar contenido QR para cada imagen

---

## 11. CONTACTO Y REFERENCIAS

- **Proyecto:** Biochar - Libertario Coffee
- **Archivo fuente:** `datos_crudos_encuesta_20250108.csv`
- **Desarrollado con:** Claude Code (Claude Opus 4.5)
- **Fecha creación:** 2026-01-11

---

*Este archivo sirve como contexto completo para retomar el proyecto en cualquier momento.*
