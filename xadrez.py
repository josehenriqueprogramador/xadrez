import streamlit as st
import chess

st.title("♟️ Xadrez Web")

# Inicializa o tabuleiro no estado da sessão do Streamlit
if 'board' not in st.session_state:
    st.session_state.board = chess.Board()

board = st.session_state.board

# Exibe o tabuleiro de forma textual (ou como código)
st.code(str(board))

st.write(f"**Turno:** {'Brancas' if board.turn else 'Pretas'}")

# Interface visual para o movimento
move = st.text_input("Digite o movimento (ex: e2e4):")

if st.button("Enviar Movimento"):
    if move:
        try:
            board.push_uci(move.strip())
            st.rerun() # Recarrega a página para atualizar o tabuleiro
        except ValueError:
            st.error("❌ Movimento inválido!")

if board.is_game_over():
    st.success("Fim de jogo!")
    if board.is_checkmate():
        st.write(f"Vencedor: {'Pretas' if board.turn else 'Brancas'}")
    elif board.is_stalemate():
        st.write("🤝 Empate!")
    
    if st.button("Reiniciar Jogo"):
        st.session_state.board = chess.Board()
        st.rerun()
