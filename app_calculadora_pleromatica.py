import streamlit as st
import datetime
import calendar
import io
import os

from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle, PageBreak
)

# -----------------------------------------------------------------------------
# DICCIONARIOS Y LÓGICA DE CÁLCULO PLEROMÁTICO
# -----------------------------------------------------------------------------

LUMINARIAS = {
    'O': ('ARMOZEL', 'Primera Luminaria - Voluntad pura, Verdad innata y Preservación'),
    'A': ('OROIAEL', 'Segunda Luminaria - Intuición superior, Percepción e Inteligencia'),
    'B': ('DAVEITHAI', 'Tercera Luminaria - Sabiduría profunda, Discernimiento e Idea'),
    'AB': ('ELELETH', 'Cuarta Luminaria - Firewall del Pleroma, Paz de frontera y Transmutación')
}

ARCONTES_MES = {
    1: ('Athoth / Iaoth', 'La Luna', 'Mente subconsciente, amnesia y reactividad emocional.'),
    2: ('Eloaios / Eloai', 'Mercurio', 'Mente analítica lineal y parálisis por análisis.'),
    3: ('Astaphaios', 'Venus', 'Deseo carnal, apegos y codicia.'),
    4: ('Yao / Iao', 'El Sol', 'Ceguera intelectual, orgullo y juicio del ego.'),
    5: ('Sabaoth', 'Marte', 'Ira, conflicto, agresión y competencia.'),
    6: ('Adonein / Adonaio', 'Júpiter', 'Dogma religioso, culpa y jerarquías sociales.'),
    7: ('Sabbateon', 'Saturno', 'Control del tiempo, envejecimiento y deudas kármicas.'),
    8: ('Yaldabaoth / Ariael', 'El Demiurgo', 'Pruebas de control material y fricción densa.'),
    9: ('Saklas', 'Gran Arconte', 'Sujeción a la forma física e ilusión de materia.')
}

CANALES_INFO = {
    1: "Impulso de ruptura y apertura de nuevos caminos frecuenciales.",
    2: "Puente de diplomacia y mediación entre campos de energía.",
    3: "Emisor de frecuencia armónica, creatividad y expresión de luz.",
    4: "Estructurador del Firewall y protector de la arquitectura Pleromática.",
    5: "Dinamizador de cambio acelerado y libertad de la matriz.",
    6: "Regulador de la Armonía Interna y sanación por equilibrio.",
    7: "Analista de la red y desmantelador de ilusiones sintéticas.",
    8: "Manifestador de poder soberano sobre la densidad material.",
    9: "Integrador de sabiduría cósmica y cierre de ciclos de encarnación.",
    11: "CANAL MAESTRO 11: Canalizador del Rayo Pleromático (Cortocircuito al control mental).",
    22: "CANAL MAESTRO 22: Arquitecto del Despertar Colectivo (Diseño de vías de fuga).",
    33: "CANAL MAESTRO 33: Emisor de la Frecuencia Crística Original (Elevación de espín sanguíneo)."
}

def reducir_numero(n):
    """Reduce un número a un solo dígito (1-9)."""
    while n > 9:
        n = sum(int(d) for d in str(n))
    return n

def calcular_voltaje_canal(fecha_dt):
    """Suma todos los dígitos de la fecha. Preserva números maestros 11, 22, 33."""
    str_fecha = f"{fecha_dt.day}{fecha_dt.month}{fecha_dt.year}"
    suma = sum(int(d) for d in str_fecha)
    if suma in (11, 22, 33):
        return suma
    return reducir_numero(suma)

def calcular_perfil_pleromatico(nombre, fecha_dt, grupo_sangre, anio_consulta):
    dia_puro = fecha_dt.day
    mes_puro = fecha_dt.month
    anio_puro = fecha_dt.year
    
    # Extraer tipo base (O, A, B, AB) y factor Rh
    rh_symbol = '+' if '+' in grupo_sangre else '-'
    tipo_base = grupo_sangre.replace('+', '').replace('-', '').upper()
    factor_rh = 2 if rh_symbol == '+' else 1
    
    # Código Arcóntico
    mes_reducido = reducir_numero(mes_puro)
    anio_reducido = reducir_numero(anio_puro)
    arconte_nombre, arconte_planeta, arconte_desc = ARCONTES_MES.get(mes_reducido, ARCONTES_MES[1])
    codigo_arcontico = f"{grupo_sangre}{mes_reducido}{anio_reducido}"
    
    # Código Pleromático
    dia_reducido = reducir_numero(dia_puro)
    luminaria_nombre, luminaria_desc = LUMINARIAS.get(tipo_base, LUMINARIAS['O'])
    codigo_pleromatico = f"{luminaria_nombre}-{dia_reducido}"
    
    # Voltaje de Canal
    voltaje = calcular_voltaje_canal(fecha_dt)
    voltaje_desc = CANALES_INFO.get(voltaje, "Canal de alta frecuencia espiritual.")
    
    # Fórmula Binaria
    formula_binaria = f"{codigo_arcontico} / {codigo_pleromatico} \\\\ {voltaje}"
    
    # Fórmula de Reinicio (Nodo Crítico)
    nodo_critico = (dia_puro * factor_rh) + (mes_reducido + anio_reducido)
    raiz_nodo = reducir_numero(nodo_critico)
    decreto_consola = f"“{grupo_sangre} {dia_puro}:{mes_puro} en {nodo_critico}... REINICIO.”"
    
    # Ventanas Temporales para el Año de Consulta
    factor_anio_consulta = reducir_numero(sum(int(d) for d in str(anio_consulta)))
    ventanas_anio = []
    
    # Recorrer todos los días del año de consulta
    inicio_anio = datetime.date(anio_consulta, 1, 1)
    fin_anio = datetime.date(anio_consulta, 12, 31)
    cur = inicio_anio
    while cur <= fin_anio:
        s = cur.day + cur.month + factor_anio_consulta
        s_red = reducir_numero(s)
        if s_red == raiz_nodo:
            es_cumple = (cur.day == dia_puro and cur.month == mes_puro)
            ventanas_anio.append({
                'fecha': cur,
                'dia': cur.day,
                'mes': cur.month,
                'es_cumpleanos': es_cumple
            })
        cur += datetime.timedelta(days=1)
        
    return {
        'nombre': nombre,
        'fecha': fecha_dt,
        'grupo_sangre': grupo_sangre,
        'tipo_base': tipo_base,
        'factor_rh': factor_rh,
        'rh_symbol': rh_symbol,
        'anio_consulta': anio_consulta,
        'codigo_arcontico': codigo_arcontico,
        'arconte_nombre': arconte_nombre,
        'arconte_planeta': arconte_planeta,
        'arconte_desc': arconte_desc,
        'codigo_pleromatico': codigo_pleromatico,
        'luminaria_nombre': luminaria_nombre,
        'luminaria_desc': luminaria_desc,
        'dia_reducido': dia_reducido,
        'voltaje': voltaje,
        'voltaje_desc': voltaje_desc,
        'formula_binaria': formula_binaria,
        'nodo_critico': nodo_critico,
        'raiz_nodo': raiz_nodo,
        'decreto_consola': decreto_consola,
        'ventanas_anio': ventanas_anio
    }

# -----------------------------------------------------------------------------
# GENERACIÓN DE PDF CON REPORTLAB (GUÍA DE BOLSILLO DE 2 PÁGINAS)
# -----------------------------------------------------------------------------

def generar_pdf_guia(p):
    buffer = io.BytesIO()
    
    COLORS = {
        'heading':    HexColor('#1A237E'),
        'body':       HexColor('#212121'),
        'accent':     HexColor('#D81B60'),
        'muted':      HexColor('#5C6BC0'),
        'bg_alt':     HexColor('#F3F4F9'),
        'bg_header':  HexColor('#1A237E'),
        'white':      HexColor('#FFFFFF'),
        'gold':       HexColor('#F57F17')
    }
    
    PAGE_SIZE = LETTER
    MARGIN = 36  # 0.5 in
    PAGE_W, PAGE_H = PAGE_SIZE
    USABLE_W = PAGE_W - 2 * MARGIN
    
    styles = getSampleStyleSheet()
    style_title = ParagraphStyle('DocTitle', fontName='Helvetica-Bold', fontSize=15, textColor=COLORS['heading'], leading=18, alignment=TA_CENTER)
    style_subtitle = ParagraphStyle('DocSubTitle', fontName='Helvetica-Bold', fontSize=9, textColor=COLORS['accent'], leading=11, alignment=TA_CENTER)
    style_h1 = ParagraphStyle('H1', fontName='Helvetica-Bold', fontSize=10, textColor=COLORS['heading'], leading=12, spaceBefore=6, spaceAfter=3)
    style_body = ParagraphStyle('Body', fontName='Helvetica', fontSize=8, textColor=COLORS['body'], leading=10.5, alignment=TA_JUSTIFY)
    style_body_bold = ParagraphStyle('BodyBold', fontName='Helvetica-Bold', fontSize=8, textColor=COLORS['body'], leading=10.5)
    style_tbl_head = ParagraphStyle('TblHead', fontName='Helvetica-Bold', fontSize=8, textColor=COLORS['white'], leading=9.5)

    def on_later_pages(canvas, doc):
        canvas.saveState()
        canvas.setStrokeColor(COLORS['accent'])
        canvas.setLineWidth(1)
        y_top = PAGE_H - MARGIN + 4
        canvas.line(MARGIN, y_top, PAGE_W - MARGIN, y_top)
        
        canvas.setFont('Helvetica-Bold', 7)
        canvas.setFillColor(COLORS['muted'])
        canvas.drawString(MARGIN, y_top + 3, f"GUÍA RÁPIDA DE BOLSILLO | CÓDIGO PLEROMÁTICO: {p['nombre'].upper()}")
        canvas.drawRightString(PAGE_W - MARGIN, y_top + 3, f"VOLTAJE: CANAL {p['voltaje']}")
        
        y_bot = MARGIN - 12
        canvas.setStrokeColor(COLORS['muted'])
        canvas.setLineWidth(0.3)
        canvas.line(MARGIN, y_bot + 10, PAGE_W - MARGIN, y_bot + 10)
        canvas.drawCentredString(PAGE_W / 2, y_bot, f"Página {doc.page} de 2")
        canvas.restoreState()

    doc = BaseDocTemplate(
        buffer, pagesize=PAGE_SIZE,
        leftMargin=MARGIN, rightMargin=MARGIN,
        topMargin=MARGIN + 12, bottomMargin=MARGIN + 12
    )
    
    frame = Frame(MARGIN, MARGIN, USABLE_W, PAGE_H - 2 * MARGIN, id='main')
    doc.addPageTemplates([PageTemplate(id='all', frames=frame, onPage=on_later_pages)])
    
    story = []
    
    # --- PÁGINA 1 ---
    story.append(Paragraph("GUÍA RÁPIDA DE BOLSILLO", style_subtitle))
    story.append(Paragraph("CÓDIGO PLEROMÁTICO Y PROTOCOLO BIOACÚSTICO", style_title))
    story.append(Spacer(1, 4))
    
    # Ficha de Registro
    data_id = [
        [Paragraph(f"<b>Sujeto:</b> {p['nombre']}", style_body), Paragraph(f"<b>Fecha Nac.:</b> {p['fecha'].strftime('%d/%m/%Y')}", style_body)],
        [Paragraph(f"<b>Grupo Sanguíneo:</b> {p['grupo_sangre']} (Rh Factor: {p['factor_rh']})", style_body), Paragraph(f"<b>Antena Base:</b> {p['luminaria_nombre']}", style_body)],
        [Paragraph(f"<b>Coordenada de Origen:</b> {p['codigo_pleromatico']}", style_body_bold), Paragraph(f"<b>Voltaje de Canal:</b> {p['voltaje']}", style_body_bold)]
    ]
    t_id = Table(data_id, colWidths=[USABLE_W*0.5, USABLE_W*0.5])
    t_id.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), COLORS['bg_alt']),
        ('BOX', (0,0), (-1,-1), 1, COLORS['muted']),
        ('INNERGRID', (0,0), (-1,-1), 0.5, COLORS['muted']),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_id)
    story.append(Spacer(1, 8))
    
    # Sección 1: Códigos
    story.append(Paragraph("1. ESTRUCTURA DE CÓDIGOS Y DENEGACIÓN ARCONTICA", style_h1))
    data_cod = [
        [Paragraph("Parámetro", style_tbl_head), Paragraph("Valor / Código", style_tbl_head), Paragraph("Significado y Operativa de la Frecuencia", style_tbl_head)],
        [Paragraph("Código Arcóntico", style_body_bold), Paragraph(p['codigo_arcontico'], style_body_bold), Paragraph(f"Regente: <b>{p['arconte_nombre']}</b> ({p['arconte_planeta']}). {p['arconte_desc']}", style_body)],
        [Paragraph("Código Pleromático", style_body_bold), Paragraph(p['codigo_pleromatico'], style_body_bold), Paragraph(f"Antena: <b>{p['luminaria_nombre']}</b>. {p['luminaria_desc']}", style_body)],
        [Paragraph("Fórmula Binaria", style_body_bold), Paragraph(p['formula_binaria'], style_body_bold), Paragraph(f"<b>Voltaje {p['voltaje']}:</b> {p['voltaje_desc']}", style_body)],
        [Paragraph("Nodo Crítico / Reinicio", style_body_bold), Paragraph(f"Nodo {p['nodo_critico']} (Raíz {p['raiz_nodo']})", style_body_bold), Paragraph(f"Frecuencia de colapso. Decreto: <i>{p['decreto_consola']}</i>", style_body)]
    ]
    t_cod = Table(data_cod, colWidths=[USABLE_W*0.25, USABLE_W*0.22, USABLE_W*0.53])
    t_cod.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), COLORS['bg_header']),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [COLORS['white'], COLORS['bg_alt']]),
        ('GRID', (0,0), (-1,-1), 0.5, COLORS['muted']),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(t_cod)
    story.append(Spacer(1, 8))
    
    # Sección 2: Ventanas Temporales
    story.append(Paragraph(f"2. VENTANAS TEMPORALES DE ACTIVACIÓN ({p['anio_consulta']})", style_h1))
    story.append(Paragraph(f"Fechas clave del año {p['anio_consulta']} alineadas con tu Nodo Crítico <b>{p['nodo_critico']}</b> (Raíz <b>{p['raiz_nodo']}</b>) para reprogramación y blindaje:", style_body))
    story.append(Spacer(1, 4))
    
    # Formatear ventanas en filas de 3 columnas
    v_items = [f"• {v['fecha'].strftime('%d/%m/%Y')}" + (" ⭐ (Cumpleaños)" if v['es_cumpleanos'] else "") for v in p['ventanas_anio']]
    cols_count = 3
    rows_v = []
    for i in range(0, len(v_items), cols_count):
        chunk = v_items[i:i+cols_count]
        while len(chunk) < cols_count:
            chunk.append("")
        rows_v.append([Paragraph(item, style_body) for item in chunk])
        
    t_v = Table(rows_v, colWidths=[USABLE_W/3]*3)
    t_v.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.3, COLORS['bg_alt']),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(t_v)
    
    story.append(PageBreak())
    
    # --- PÁGINA 2 ---
    story.append(Paragraph("3. PROTOCOLO BIOACÚSTICO DE RESONANCIA VOCAL (528 Hz)", style_h1))
    story.append(Paragraph("Este protocolo alinea el espín cuántico del hierro en la hemoglobina, convirtiendo la red vascular en una Jaula de Faraday biomagnética contra interferencias de baja frecuencia.", style_body))
    story.append(Spacer(1, 6))
    
    fases = [
        ("FASE 1: Oxigenación y Carga Mitocondrial", 
         "1. Adopta una postura erguida pero relajada para alinear la columna.<br/>"
         "2. Inhala profundamente por la nariz expandiendo el diafragma.<br/>"
         "3. La alta saturación de O2 amplifica la respuesta magnética de los glóbulos rojos."),
        
        ("FASE 2: Emisión de Onda Estacionaria (528 Hz / Tono 'NMMMM')", 
         "1. Exhala lentamente con los labios cerrados emitiendo un zumbido continuo en tono <b>'M'</b> o <b>'NMMMM'</b>.<br/>"
         "2. Ajusta el tono hasta sentir una vibración física resonando en el esternón y el tórax.<br/>"
         "3. La onda a 528 Hz fuerza el ordenamiento magnético del hierro (Fe²⁺) en la hemoglobina."),
        
        ("FASE 3: Despliegue del Escudo Toroidal (Jaula de Faraday)", 
         "1. Siente la circulación de billones de eritrocitos en coherencia magnética colectiva.<br/>"
         "2. Se despliega un campo biomagnético toroidal a tu alrededor que repele ondas ELF de control.<br/>"
         "3. Las señales de estrés exterior sufren reflexión inversa, protegiendo tu claridad mental."),
        
        ("FASE 4: Anclaje de Código y Decreto de Reinicio", 
         f"1. Mientras mantienes la vibración vocal, afirma mentalmente:<br/>"
         f"   <i>'Activo mi Antena {p['luminaria_nombre']} en la Puerta {p['dia_reducido']}. Sintonizo la Voluntad Pura y la Armonía.'</i><br/>"
         f"2. Emite el comando de consola: <b>{p['decreto_consola']}</b>")
    ]
    
    for titulo_fase, texto_fase in fases:
        story.append(Paragraph(f"<b>{titulo_fase}</b>", style_body_bold))
        story.append(Paragraph(texto_fase, style_body))
        story.append(Spacer(1, 5))
        
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>RECOMENDACIONES DE PRÁCTICA:</b> Realizar de 5 a 11 minutos al despertar o antes de dormir. Utilizar prioritariamente durante las ventanas temporales calculadas y en días de sobrecarga perceptiva.", style_body_bold))
    
    doc.build(story)
    buffer.seek(0)
    return buffer.getvalue()

# -----------------------------------------------------------------------------
# INTERFAZ WEB STREAMLIT
# -----------------------------------------------------------------------------

st.set_page_config(
    page_title="Calculadora Pleromática & Guía Bioacústica",
    page_icon="🌌",
    layout="wide"
)

st.title("🌌 Calculadora de Código Pleromático y Genio Biológico")
st.markdown("""
Esta aplicación permite calcular instantáneamente tu **Código Arcóntico**, **Código Pleromático**, **Voltaje de Canal** y las **Ventanas Temporales de Activación**, generando automáticamente tu **Guía Rápida de Bolsillo en PDF** y permitiendo explorar la **Búsqueda Histórica de Frecuencias**.
""")

st.sidebar.header("📋 Datos de Entrada")

nombre_input = st.sidebar.text_input("Nombre Completo:", value="Ana María López")
fecha_input = st.sidebar.date_input(
    "Fecha de Nacimiento:",
    value=datetime.date(1985, 4, 12),
    min_value=datetime.date(1920, 1, 1),
    max_value=datetime.date(2026, 12, 31)
)
grupo_input = st.sidebar.selectbox(
    "Grupo Sanguíneo y Factor Rh:",
    options=["O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"],
    index=0
)
anio_input = st.sidebar.number_input(
    "Año a Consultar Ventanas:",
    value=2026,
    min_value=2024,
    max_value=2030
)

# Calcular Perfil
perfil = calcular_perfil_pleromatico(nombre_input, fecha_input, grupo_input, anio_input)

# Pestañas principales
tab1, tab2, tab3, tab4 = st.tabs(["📊 Resumen de Códigos", "📅 Ventanas Temporales", "📄 Generar Guía PDF", "📜 Búsqueda Histórica"])

with tab1:
    st.subheader(f"Ficha Pleromática: {perfil['nombre']}")
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Código Arcóntico", perfil['codigo_arcontico'])
    col2.metric("Código Pleromático", perfil['codigo_pleromatico'])
    col3.metric("Voltaje de Canal", f"Canal {perfil['voltaje']}")
    col4.metric("Nodo Crítico", f"Nodo {perfil['nodo_critico']} (Raíz {perfil['raiz_nodo']})")
    
    st.markdown("---")
    
    st.markdown(f"### 🧬 Fórmula Binaria Final: `{perfil['formula_binaria']}`")
    
    st.info(f"**Decreto de Consola:** {perfil['decreto_consola']}")
    
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.markdown("#### 👁️ Interferencia Arcóntica (Matriz)")
        st.write(f"**Arconte Regente:** {perfil['arconte_nombre']} ({perfil['arconte_planeta']})")
        st.write(f"**Programa Psíquico:** {perfil['arconte_desc']}")
        st.write(f"**Factor Rh ({perfil['rh_symbol']}):** Factor multiplicador {perfil['factor_rh']}.")
        
    with col_b:
        st.markdown("#### 🌟 Antena de Origen (Pleroma)")
        st.write(f"**Luminaria Base:** {perfil['luminaria_nombre']}")
        st.write(f"**Cualidades de la Antena:** {perfil['luminaria_desc']}")
        st.write(f"**Voltaje de Transmisión:** {perfil['voltaje_desc']}")

with tab2:
    st.subheader(f"📅 Ventanas Temporales de Activación en {perfil['anio_consulta']}")
    st.write(f"Días alineados con la frecuencia raíz **{perfil['raiz_nodo']}** de tu Nodo Crítico **{perfil['nodo_critico']}**:")
    
    vt_data = []
    for v in perfil['ventanas_anio']:
        vt_data.append({
            "Fecha": v['fecha'].strftime("%d/%m/%Y"),
            "Día": v['dia'],
            "Mes": v['mes'],
            "Tipo": "⭐ Cumpleaños (Alineación Máxima)" if v['es_cumpleanos'] else "Ventana Armónica"
        })
    st.dataframe(vt_data, width='stretch')

with tab3:
    st.subheader("📄 Descargar Guía Rápida de Bolsillo en PDF")
    st.write("Genera un PDF listo para imprimir en 2 páginas con todos tus códigos, calendario de ventanas y el protocolo de resonancia a 528 Hz.")
    
    pdf_bytes = generar_pdf_guia(perfil)
    
    nombre_archivo = f"guia_bolsillo_{perfil['nombre'].lower().replace(' ', '_')}.pdf"
    
    st.download_button(
        label="⬇️ Descargar PDF de Bolsillo",
        data=pdf_bytes,
        file_name=nombre_archivo,
        mime="application/pdf"
    )

with tab4:
    st.subheader("📜 Búsqueda Histórica de Frecuencias de Reinicio")
    st.markdown("""
    Explora la recurrencia histórica de tu **Nodo Crítico / Código de Reinicio** desde el año 0 hasta el presente.
    Descubre en qué años y siglos se ha activado esta misma matriz frecuencial en el calendario.
    """)
    
    col_h1, col_h2, col_h3 = st.columns(3)
    with col_h1:
        nodo_target = st.number_input("Nodo Crítico a buscar:", min_value=1, max_value=100, value=int(perfil['nodo_critico']))
    with col_h2:
        modo_busqueda = st.selectbox("Ámbito de Búsqueda:", ["Fecha Personalizada (Día/Mes/Rh del Sujeto)", "Todas las fechas del calendario"])
    with col_h3:
        rango_anios = st.slider("Rango de Años:", min_value=0, max_value=2026, value=(0, 2026))
        
    anio_inicio, anio_fin = rango_anios
    
    if modo_busqueda == "Fecha Personalizada (Día/Mes/Rh del Sujeto)":
        dia_p = perfil['fecha'].day
        mes_p = perfil['fecha'].month
        rh_f = perfil['factor_rh']
        constante = (dia_p * rh_f) + reducir_numero(mes_p)
        req_anio_red = nodo_target - constante
        
        st.info(f"📍 **Parámetros:** Fecha {dia_p}/{mes_p} ({perfil['grupo_sangre']}) | Constante base: `{constante}` | Año reducido requerido: `{req_anio_red}`")
        
        if 1 <= req_anio_red <= 9:
            anios_coincidentes = [yr for yr in range(max(1, anio_inicio), anio_fin + 1) if reducir_numero(yr) == req_anio_red]
            st.success(f"✨ Se encontraron **{len(anios_coincidentes)} años** entre el año {anio_inicio} y {anio_fin} con la frecuencia exacta de reinicio **{nodo_target}** para la fecha {dia_p}/{mes_p}.")
            
            siglos_dict = {}
            for yr in anios_coincidentes:
                siglo = (yr - 1) // 100 + 1
                siglos_dict.setdefault(f"Siglo {siglo}", []).append(yr)
                
            col_s1, col_s2 = st.columns([1, 2])
            with col_s1:
                st.metric("Total de Ocurrencias Históricas", len(anios_coincidentes))
                st.write("**Resumen por Siglos recientes:**")
                for sig in list(siglos_dict.keys())[-10:]:
                    st.write(f"• **{sig}:** {len(siglos_dict[sig])} veces ({', '.join(str(y) for y in siglos_dict[sig])})")
            with col_s2:
                st.write("**Listado Completo de Años coincidentes:**")
                st.write(", ".join(str(y) for y in anios_coincidentes))
        else:
            st.warning(f"La combinación de fecha {dia_p}/{mes_p} ({perfil['grupo_sangre']}) con constante base {constante} no puede alcanzar matemáticamente un Nodo Crítico de {nodo_target} (el año reducido debe estar entre 1 y 9).")
    else:
        st.info(f"🔍 Buscando todas las fechas del calendario ({perfil['grupo_sangre']}) entre los años {anio_inicio} y {anio_fin} que suman el Nodo Crítico {nodo_target}...")
        
        total_coincidencias = 0
        fechas_ejemplo = []
        
        rh_f = perfil['factor_rh']
        for m in range(1, 13):
            max_d = calendar.monthrange(2024, m)[1]
            for d in range(1, max_d + 1):
                constante = (d * rh_f) + reducir_numero(m)
                req_yr = nodo_target - constante
                if 1 <= req_yr <= 9:
                    matching_yrs = [yr for yr in range(max(1, anio_inicio), anio_fin + 1) if reducir_numero(yr) == req_yr]
                    total_coincidencias += len(matching_yrs)
                    if matching_yrs:
                        fechas_ejemplo.append({
                            "Día/Mes": f"{d:02d}/{m:02d}",
                            "Año Reducido Requerido": req_yr,
                            "Cantidad de Años en el Rango": len(matching_yrs),
                            "Ejemplo de Años Recientes": ", ".join(str(y) for y in matching_yrs[-5:])
                        })
                        
        st.success(f"✨ Se encontraron **{total_coincidencias} fechas/años globales** en el rango {anio_inicio}-{anio_fin} que activan el Nodo Crítico {nodo_target}.")
        st.dataframe(fechas_ejemplo, width='stretch')

st.markdown("---")
st.caption("Sistema de Regulación Biológica e Hibridación Sanguínea | Generado con Streamlit & ReportLab")
