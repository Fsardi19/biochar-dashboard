# CLAUDE.md - Biochar Dashboard

## Sobre el Proyecto
Dashboard de analisis de encuesta sobre el Proyecto Biochar de Libertario Coffee. El 3% de las ventas financia biochar en fincas cafeteras.

## Repositorio
- GitHub: https://github.com/Fsardi19/biochar-dashboard
- Dashboard: https://biochar-dashboard-tiw6cdz2wcjbcrjto4ssev.streamlit.app/
- Guia HTML: https://fsardi19.github.io/biochar-dashboard/GUIA_COMUNICACION_BIOCHAR_V2.html

## Reglas Importantes

### Mensaje del Proyecto
- CORRECTO: "El 3% de cada venta financia la produccion de biochar en fincas cafeteras"
- INCORRECTO: "Compramos cafe de fincas con biochar" (NO es asi)

### Branding Libertario Coffee
- Azul oscuro: #182b55
- Beige: #e8e4de
- Dorado: #c9a227
- Tipografia: Libre Baskerville
- Tono: Emocional, inspiracional, no tecnico

### Datos Clave
- 836 encuestados validos
- 12 tiendas (10 CO, 1 CR, 2 MX)
- 91% satisfaccion global
- 22% conocia el proyecto

### Alertas Activas
- CR-Escalante: 71.4% satisfaccion (20 puntos bajo promedio)
- Requiere investigacion y plan de recuperacion

## Estructura de Archivos
```
biochar-dashboard/
├── app.py                          # Dashboard Streamlit
├── requirements.txt                # Dependencias
├── PROJECT_CONTEXT.md              # Contexto completo
├── GUIA_COMUNICACION.md            # Lineamientos Emilio
├── GUIA_COMUNICACION_POR_PAIS.md   # Guia practica CO/CR/MX
├── GUIA_COMUNICACION_BIOCHAR_V2.html # Guia visual
├── data/
│   ├── metricas_biochar.json
│   └── metricas_por_tienda.json
└── .claude/
    ├── SESSION_LOG.md
    └── PROGRESO.md
```

## Comandos Utiles
```bash
# Correr dashboard local
streamlit run app.py

# Convertir .docx a texto (macOS)
textutil -stdout -convert txt archivo.docx
```

## Contacto
- Cliente: Libertario Coffee
- Proyecto: The Green Hub
