"""
Biochar Insights Dashboard - Libertario Coffee
Análisis de Percepción del Proyecto Biochar
"""

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import json
import os

# ========================================
# CONFIGURACIÓN
# ========================================

st.set_page_config(
    page_title="Biochar Insights - Libertario Coffee",
    page_icon="☕",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Colores de marca Libertario
COLORS = {
    "verde_oscuro": "#2C5530",
    "verde_claro": "#4A7C59",
    "cafe": "#8B4513",
    "beige": "#F5DEB3",
    "crema": "#FFF8DC",
    "rojo": "#C0392B",
    "amarillo": "#F39C12"
}

PALETTE = ["#2C5530", "#4A7C59", "#8B4513", "#D2691E", "#F5DEB3"]

# ========================================
# CARGAR DATOS
# ========================================

@st.cache_data
def cargar_datos():
    base_path = os.path.dirname(__file__)

    with open(os.path.join(base_path, "data/metricas_biochar.json"), 'r', encoding='utf-8') as f:
        metricas = json.load(f)

    with open(os.path.join(base_path, "data/metricas_por_tienda.json"), 'r', encoding='utf-8') as f:
        tiendas = json.load(f)

    return metricas, tiendas

metricas, tiendas_data = cargar_datos()
tiendas = tiendas_data['tiendas']

# Orden de tiendas por satisfacción
STORE_ORDER = [
    "CO - Getsemani", "MX - Colima 340", "CO - FIC48", "CO - Calle 85",
    "CO - Usaquen", "MX - Roma Norte", "CO - 122 B", "CO - Calle 109",
    "CO - Zona G", "CO - Calle 79", "CO - Calle 93", "CR - Escalante"
]

# ========================================
# CSS PERSONALIZADO
# ========================================

st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #2C5530;
        text-align: center;
        padding: 1rem 0;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #8B4513;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #2C5530 0%, #4A7C59 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        text-align: center;
    }
    .insight-box {
        background-color: #FFF8DC;
        border-left: 4px solid #2C5530;
        padding: 1rem;
        margin: 0.5rem 0;
        border-radius: 0 8px 8px 0;
    }
    .insight-box.warning {
        border-left-color: #F39C12;
        background-color: #FEF9E7;
    }
    .insight-box.alert {
        border-left-color: #C0392B;
        background-color: #FDEDEC;
    }
    .mensaje-box {
        background: linear-gradient(135deg, #2C5530 0%, #4A7C59 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        font-size: 1.1rem;
        line-height: 1.6;
        margin: 1rem 0;
    }
    .store-card {
        background: white;
        border-radius: 10px;
        padding: 1rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        border-left: 4px solid #2C5530;
        margin-bottom: 0.5rem;
    }
    .store-card.warning {
        border-left-color: #F39C12;
    }
    .store-card.alert {
        border-left-color: #C0392B;
    }
</style>
""", unsafe_allow_html=True)

# ========================================
# SIDEBAR
# ========================================

with st.sidebar:
    st.image("https://via.placeholder.com/200x60/2C5530/FFFFFF?text=Libertario+Coffee", use_container_width=True)
    st.markdown("---")

    st.markdown("### Navegación")
    pagina = st.radio(
        "Selecciona vista:",
        ["📊 Vista Ejecutiva", "🏪 Todas las Tiendas", "🔍 Análisis por Tienda", "💬 Mensajes Sugeridos", "💡 Insights"],
        label_visibility="collapsed"
    )

    st.markdown("---")
    st.markdown(f"**Período:** 2025-11-11 → 2026-01-07")
    st.markdown(f"**Total:** {metricas['kpis']['total_encuestados']} encuestados")
    st.markdown(f"**Tiendas:** 12 en 3 países")

# ========================================
# HEADER
# ========================================

st.markdown('<p class="main-header">☕ Biochar Insights</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Análisis de Percepción del Proyecto Biochar - Libertario Coffee</p>', unsafe_allow_html=True)

# ========================================
# PÁGINA: VISTA EJECUTIVA
# ========================================

if pagina == "📊 Vista Ejecutiva":

    # KPIs
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Encuestados", f"{metricas['kpis']['total_encuestados']:,}", "3 países")
    with col2:
        st.metric("Conocía Iniciativa", f"{metricas['kpis']['pct_conocia_iniciativa']}%", "Oportunidad")
    with col3:
        st.metric("Me encanta/gusta", f"{metricas['kpis']['pct_me_encanta_gusta']}%", "Alta aprobación")
    with col4:
        st.metric("Influye en Retorno", f"{metricas['kpis']['pct_influye_bastante_mucho']}%", "Bastante/Decisivo")

    st.markdown("---")

    # Gráficos principales
    col_left, col_right = st.columns(2)

    with col_left:
        st.markdown("#### Opinión sobre destinar 3% a Biochar")

        opinion_data = metricas['opinion_3_porciento']['distribucion']
        orden = ["Me encanta", "Me gusta", "Me gusta poco", "No me gusta nada"]

        fig_dona = go.Figure(data=[go.Pie(
            labels=[k for k in orden if k in opinion_data],
            values=[opinion_data.get(k, 0) for k in orden if k in opinion_data],
            hole=0.5,
            marker_colors=PALETTE,
            textinfo='percent+label',
            textposition='outside'
        )])
        fig_dona.update_layout(showlegend=False, height=400, margin=dict(t=20, b=20))
        st.plotly_chart(fig_dona, use_container_width=True)

    with col_right:
        st.markdown("#### Ranking de Beneficios Biochar")

        ranking = metricas['beneficios_biochar']['ranking'][:10]

        fig_ranking = go.Figure(go.Bar(
            x=[item['promedio'] for item in reversed(ranking)],
            y=[item['nombre'][:25] for item in reversed(ranking)],
            orientation='h',
            marker_color=COLORS['verde_oscuro'],
            text=[f"{item['promedio']:.2f}" for item in reversed(ranking)],
            textposition='outside'
        ))
        fig_ranking.update_layout(
            height=400,
            margin=dict(t=20, b=20, l=20, r=80),
            xaxis_range=[3.5, 5]
        )
        st.plotly_chart(fig_ranking, use_container_width=True)

    # Satisfacción por tienda
    st.markdown("---")
    st.markdown("#### Satisfacción por Tienda")

    satisfaccion_data = [(s, tiendas[s]['metricas']['pct_satisfaccion']) for s in STORE_ORDER if s in tiendas]

    fig_sat = go.Figure(go.Bar(
        x=[s.split(' - ')[1] for s, _ in satisfaccion_data],
        y=[v for _, v in satisfaccion_data],
        marker_color=[COLORS['verde_oscuro'] if v >= 95 else COLORS['verde_claro'] if v >= 90 else COLORS['amarillo'] if v >= 80 else COLORS['rojo'] for _, v in satisfaccion_data],
        text=[f"{v}%" for _, v in satisfaccion_data],
        textposition='outside'
    ))
    fig_sat.update_layout(
        height=400,
        yaxis_range=[0, 110],
        xaxis_tickangle=-45,
        shapes=[dict(type='line', x0=-0.5, x1=11.5, y0=91, y1=91, line=dict(color='#666', width=2, dash='dash'))],
        annotations=[dict(x=10, y=93, text='Promedio: 91%', showarrow=False, font=dict(size=11))]
    )
    st.plotly_chart(fig_sat, use_container_width=True)

# ========================================
# PÁGINA: TODAS LAS TIENDAS
# ========================================

elif pagina == "🏪 Todas las Tiendas":

    st.markdown("### Resumen de Todas las Tiendas")
    st.markdown("*Click en una tienda en el selector lateral para ver detalles*")

    # Grid de tiendas
    for i in range(0, len(STORE_ORDER), 3):
        cols = st.columns(3)
        for j, col in enumerate(cols):
            if i + j < len(STORE_ORDER):
                store_name = STORE_ORDER[i + j]
                if store_name in tiendas:
                    t = tiendas[store_name]
                    m = t['metricas']

                    status = "🟢" if m['pct_satisfaccion'] >= 95 else "🟡" if m['pct_satisfaccion'] >= 85 else "🔴"

                    with col:
                        st.markdown(f"""
                        <div class="store-card {'alert' if m['pct_satisfaccion'] < 80 else 'warning' if m['pct_satisfaccion'] < 90 else ''}">
                            <strong>{status} {store_name}</strong><br>
                            <small>n={t['n']} | Satisf: {m['pct_satisfaccion']}% | Influye: {m['pct_influye_alto']}%</small><br>
                            <small><em>Top: {t['beneficios']['top_3'][0]['nombre']}</em></small>
                        </div>
                        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### Tabla Comparativa")

    # Tabla comparativa
    table_data = []
    for store_name in STORE_ORDER:
        if store_name in tiendas:
            t = tiendas[store_name]
            m = t['metricas']
            table_data.append({
                "Tienda": store_name,
                "n": t['n'],
                "Satisfacción": f"{m['pct_satisfaccion']}%",
                "Conocía": f"{m['pct_conocia']}%",
                "Influye Retorno": f"{m['pct_influye_alto']}%",
                "Top Beneficio": t['beneficios']['top_3'][0]['nombre']
            })

    st.dataframe(table_data, use_container_width=True, hide_index=True)

# ========================================
# PÁGINA: ANÁLISIS POR TIENDA
# ========================================

elif pagina == "🔍 Análisis por Tienda":

    st.markdown("### Análisis Detallado por Tienda")

    tienda_seleccionada = st.selectbox(
        "Selecciona una tienda:",
        options=STORE_ORDER,
        format_func=lambda x: f"{x} (n={tiendas[x]['n']})" if x in tiendas else x
    )

    if tienda_seleccionada and tienda_seleccionada in tiendas:
        t = tiendas[tienda_seleccionada]
        m = t['metricas']

        st.markdown("---")

        # KPIs de la tienda
        col1, col2, col3, col4, col5, col6 = st.columns(6)
        col1.metric("Encuestados", t['n'])
        col2.metric("Satisfacción", f"{m['pct_satisfaccion']}%")
        col3.metric("Conocía", f"{m['pct_conocia']}%")
        col4.metric("Influye Retorno", f"{m['pct_influye_alto']}%")
        col5.metric("Primera Vez", f"{m['pct_primera_vez']}%")
        col6.metric("Recurrentes", f"{m['pct_recurrente']}%")

        st.markdown("---")

        # Top 3 y Bottom 3
        col_left, col_right = st.columns(2)

        with col_left:
            st.markdown("#### 🏆 Top 3 Beneficios")
            for i, b in enumerate(t['beneficios']['top_3'], 1):
                st.markdown(f"""
                <div class="insight-box">
                    <strong>{i}. {b['nombre']}</strong> — Promedio: {b['promedio']}/5
                </div>
                """, unsafe_allow_html=True)

        with col_right:
            st.markdown("#### ⚠️ Beneficios menos valorados")
            for b in t['beneficios']['bottom_3']:
                st.markdown(f"""
                <div class="insight-box warning">
                    <strong>{b['nombre']}</strong> — Promedio: {b['promedio']}/5
                </div>
                """, unsafe_allow_html=True)

        st.markdown("---")

        # Insights y Recomendaciones
        col_left, col_right = st.columns(2)

        with col_left:
            st.markdown("#### 💡 Insights")
            for insight in t['insights']:
                alert_class = "alert" if "🚨" in insight or "⚠️" in insight else ""
                st.markdown(f"""
                <div class="insight-box {alert_class}">
                    {insight}
                </div>
                """, unsafe_allow_html=True)

        with col_right:
            st.markdown("#### 🎯 Recomendaciones")
            for rec in t['recomendaciones']:
                st.markdown(f"""
                <div class="insight-box">
                    ✅ {rec}
                </div>
                """, unsafe_allow_html=True)

        st.markdown("---")

        # Mensaje sugerido
        st.markdown("#### 💬 Mensaje Sugerido para esta Tienda")
        st.markdown(f"""
        <div class="mensaje-box">
            <small>Usa este mensaje en materiales de la tienda:</small><br><br>
            "{t['mensaje_sugerido']}"
        </div>
        """, unsafe_allow_html=True)

        st.markdown("---")

        # Gráficos
        st.markdown("#### 📊 Ranking de Beneficios")

        ranking = t['beneficios']['ranking']
        fig_ben = go.Figure(go.Bar(
            x=[b['nombre'][:20] for b in ranking],
            y=[b['promedio'] for b in ranking],
            marker_color=[COLORS['verde_oscuro'] if b['promedio'] >= 4.5 else COLORS['verde_claro'] if b['promedio'] >= 4 else COLORS['cafe'] for b in ranking],
            text=[f"{b['promedio']:.2f}" for b in ranking],
            textposition='outside'
        ))
        fig_ben.update_layout(height=350, yaxis_range=[3, 5.2], xaxis_tickangle=-45)
        st.plotly_chart(fig_ben, use_container_width=True)

        # Distribución de opinión e influencia
        col_left, col_right = st.columns(2)

        with col_left:
            st.markdown("#### Distribución de Opinión")
            fig_op = go.Figure(data=[go.Pie(
                labels=['Me encanta', 'Me gusta', 'Me gusta poco', 'No me gusta'],
                values=[m['pct_me_encanta'], m['pct_me_gusta'], m['pct_me_gusta_poco'], m['pct_no_me_gusta']],
                marker_colors=PALETTE,
                textinfo='percent+label'
            )])
            fig_op.update_layout(height=300, showlegend=False)
            st.plotly_chart(fig_op, use_container_width=True)

        with col_right:
            st.markdown("#### Influencia en Retorno")
            fig_inf = go.Figure(go.Bar(
                x=['Decisivo', 'Bastante', 'Poco', 'No influye'],
                y=[m['pct_influye_decisivo'], m['pct_influye_bastante'], m['pct_influye_poco'], m['pct_no_influye']],
                marker_color=[COLORS['verde_oscuro'], COLORS['verde_claro'], COLORS['beige'], COLORS['cafe']],
                text=[f"{v}%" for v in [m['pct_influye_decisivo'], m['pct_influye_bastante'], m['pct_influye_poco'], m['pct_no_influye']]],
                textposition='outside'
            ))
            fig_inf.update_layout(height=300, yaxis_range=[0, 80])
            st.plotly_chart(fig_inf, use_container_width=True)

# ========================================
# PÁGINA: MENSAJES SUGERIDOS
# ========================================

elif pagina == "💬 Mensajes Sugeridos":

    st.markdown("### Mensajes de Comunicación por Tienda")
    st.markdown("*Mensajes personalizados basados en el perfil de cada tienda*")

    for store_name in STORE_ORDER:
        if store_name in tiendas:
            t = tiendas[store_name]
            m = t['metricas']

            with st.expander(f"**{store_name}** — Satisf: {m['pct_satisfaccion']}% | Driver: {t['beneficios']['top_3'][0]['nombre']}", expanded=False):
                st.markdown(f"""
                <div class="mensaje-box">
                    "{t['mensaje_sugerido']}"
                </div>
                """, unsafe_allow_html=True)

                st.markdown(f"""
                **Driver #1:** {t['beneficios']['top_3'][0]['nombre']}
                **Satisfacción:** {m['pct_satisfaccion']}%
                **Influye en retorno:** {m['pct_influye_alto']}%
                **Perfil:** {m['pct_recurrente']}% recurrentes, {m['pct_primera_vez']}% primera vez
                """)

# ========================================
# PÁGINA: INSIGHTS
# ========================================

elif pagina == "💡 Insights":

    st.markdown("### 🚨 Alertas y Prioridades")

    st.markdown("""
    <div class="insight-box alert">
        <strong>⚠️ CR - Escalante: Requiere atención urgente</strong><br>
        Satisfacción de solo 71.4% (vs 91% promedio). El 28.6% dice "Me gusta poco" o "No me gusta".<br>
        <strong>Acción:</strong> Investigar con equipo local las causas. Posible desconexión con el concepto de biochar.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="insight-box warning">
        <strong>⚡ CO - Calle 93: Bajo awareness pero base leal</strong><br>
        Solo 19.5% conocía la iniciativa, pero 88.3% son recurrentes. Oportunidad de educar a clientes fieles.<br>
        <strong>Acción:</strong> Campaña de educación sobre biochar con material visual.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="insight-box">
        <strong>🌟 CO - Calle 85: Tienda modelo</strong><br>
        95.7% satisfacción, 80.9% dice que influye en retorno, 38.3% conocía la iniciativa.<br>
        <strong>Acción:</strong> Documentar mejores prácticas y replicar en otras tiendas.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 🏆 Top 3 Beneficios que Más Resuenan")

    for i, item in enumerate(metricas['beneficios_biochar']['ranking'][:3], 1):
        st.markdown(f"""
        <div class="insight-box">
            <strong>{i}. {item['nombre']}</strong> — Promedio: {item['promedio']}/5 | {item['promotores_pct']}% promotores
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 🎯 Recomendaciones Estratégicas")

    recomendaciones = [
        ("Personalizar mensajes por tienda", "Cada tienda tiene un beneficio #1 diferente. Usar el ranking local en comunicación."),
        ("Aumentar awareness de forma masiva", "78% no conocía la iniciativa. Gran oportunidad con material visual en tiendas."),
        ("Enfocarse en 'mejor sabor' donde aplique", "En CO - Calle 93 y CO - FIC48 el sabor es el beneficio #1. Usar catas comparativas."),
        ("Tiendas con alta influencia = embajadores", "CO - Calle 85 (80.9%), MX - Roma Norte (80.0%), CO - Calle 79 (77.1%) pueden generar referidos.")
    ]

    for titulo, desc in recomendaciones:
        st.markdown(f"""
        <div class="insight-box">
            <strong>✅ {titulo}</strong><br>
            {desc}
        </div>
        """, unsafe_allow_html=True)

# ========================================
# FOOTER
# ========================================

st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #8B4513; padding: 1rem;">
    <small>Dashboard generado para Libertario Coffee | Proyecto Biochar 2025-2026</small>
</div>
""", unsafe_allow_html=True)
