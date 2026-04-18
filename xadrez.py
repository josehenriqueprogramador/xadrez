import streamlit as st
import chess
import chess.svg
import base64

def render_svg(svg):
    """Renderiza o SVG no Streamlit"""
    b64 = base64.b64encode(svg.encode('utf-8')).decode("utf-8")
    html = f'<img src="data:image/svg+xml;base64,{b64}" width="500px"/>' # Tamanho ampliado aqui
    return html

st.set_page_config(page_title="Xadrez Premium", layout="centered")
st.title("♟️ Xadrez Web Profissional")

# 1. Inicialização do Estado
if 'board' not in st.session_state:
    st.session_state.board = chess.Board()

board = st.session_state.board

# 2. Lógica das Regras Mencionadas
# O 'python-chess' já segue por padrão as regras da FIDE:
# - Casa branca (h1/a8) no lado direito do jogador.
# - Rei Branco na casa preta (e1) e Rei Preto na casa branca (e8).

# 3. Renderização Visual com SVG
# 'size' controla a resolução do desenho interno
board_svg = chess.svg.board(board=board, size=600) 
st.write(render_svg(board_svg), unsafe_allow_html=True)

st.write(f"### **Turno:** {'⚪ Brancas' if board.turn else '⚫ Pretas'}")

# 4. Interface de Jogada
col1, col2 = st.columns([3, 1])
with col1:
    move = st.text_input("Digite o movimento (ex: e2e4):", key="move_input")
with col2:
    st.write("##") # Espaçamento
    btn_move = st.button("Mover")

if btn_move:
    if move:
        try:
            # Tenta converter a string para um movimento legal
            chess_move = chess.Move.from_uci(move.strip())
            if chess_move in board.legal_moves:
                board.push(chess_move)
                st.rerun()
            else:
                st.error("⚠️ Movimento ilegal!")
        except ValueError:
            st.error("❌ Formato inválido! Use o padrão e2e4.")

# 5. Status do Jogo
if board.is_game_over():
    st.divider()
    st.warning("🏁 Fim de Jogo!")
    resultado = board.result()
    st.info(f"Resultado final: {resultado}")
    
    if st.button("Reiniciar Partida"):
        st.session_state.board = chess.Board()
        st.rerun()

# 6. Histórico (Opcional, mas ajuda visualmente)
if len(board.move_stack) > 0:
    with st.expander("Ver Histórico de Movimentos"):
        st.write(board.move_stack)
