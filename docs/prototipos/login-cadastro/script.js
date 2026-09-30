const KEY_USERS = "demo_users";
const KEY_SESSION = "demo_session";

function lerUsuarios() {
  try { return JSON.parse(localStorage.getItem(KEY_USERS)) || []; }
  catch { return []; }
}
function salvarUsuarios(lista) {
  try { localStorage.setItem(KEY_USERS, JSON.stringify(lista)); return true; }
  catch { return false; }
}
function lerSessao() {
  try { return localStorage.getItem(KEY_SESSION); } catch { return null; }
}
function salvarSessao(email) {
  try {
    if (email) localStorage.setItem(KEY_SESSION, email);
    else localStorage.removeItem(KEY_SESSION);
  } catch {}
}

// Hash da senha (SHA-256) para não guardar a senha em texto puro
async function hash(texto) {
  if (!(window.crypto && crypto.subtle)) return texto;
  const buf = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(texto));
  return Array.from(new Uint8Array(buf)).map(b => b.toString(16).padStart(2, "0")).join("");
}

// ---------- Navegação entre telas ----------
const views = {
  login: document.getElementById("login-view"),
  signup: document.getElementById("signup-view"),
  welcome: document.getElementById("welcome-view"),
};
function mostrar(nome) {
  Object.entries(views).forEach(([k, el]) => el.classList.toggle("hidden", k !== nome));
  document.querySelectorAll(".msg").forEach(m => { m.textContent = ""; m.className = "msg"; });
}
document.querySelectorAll("[data-go]").forEach(btn =>
  btn.addEventListener("click", () => mostrar(btn.dataset.go))
);

function mensagem(id, texto, tipo) {
  const el = document.getElementById(id);
  el.textContent = texto;
  el.className = "msg " + tipo;
}
const emailValido = e => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(e);

function entrar(usuario) {
  salvarSessao(usuario.email);
  document.getElementById("welcome-title").textContent = "Olá, " + usuario.nome + "!";
  mostrar("welcome");
}

// ---------- Cadastro ----------
document.getElementById("signup-form").addEventListener("submit", async (e) => {
  e.preventDefault();
  const nome = document.getElementById("signup-nome").value.trim();
  const email = document.getElementById("signup-email").value.trim().toLowerCase();
  const senha = document.getElementById("signup-senha").value;
  const confirma = document.getElementById("signup-confirma").value;

  if (!nome) return mensagem("signup-msg", "Informe seu nome.", "error");
  if (!emailValido(email)) return mensagem("signup-msg", "E-mail inválido.", "error");
  if (senha.length < 6) return mensagem("signup-msg", "A senha deve ter ao menos 6 caracteres.", "error");
  if (senha !== confirma) return mensagem("signup-msg", "As senhas não coincidem.", "error");

  const usuarios = lerUsuarios();
  if (usuarios.some(u => u.email === email))
    return mensagem("signup-msg", "Este e-mail já está cadastrado.", "error");

  usuarios.push({ nome, email, senha: await hash(senha) });
  if (!salvarUsuarios(usuarios))
    return mensagem("signup-msg", "Não foi possível salvar o cadastro.", "error");

  e.target.reset();
  mostrar("login");
  mensagem("login-msg", "Cadastro realizado! Faça login.", "ok");
});

// ---------- Login ----------
document.getElementById("login-form").addEventListener("submit", async (e) => {
  e.preventDefault();
  const email = document.getElementById("login-email").value.trim().toLowerCase();
  const senha = document.getElementById("login-senha").value;

  if (!emailValido(email) || !senha)
    return mensagem("login-msg", "Preencha e-mail e senha.", "error");

  const senhaHash = await hash(senha);
  const usuario = lerUsuarios().find(u => u.email === email && u.senha === senhaHash);
  if (!usuario) return mensagem("login-msg", "E-mail ou senha incorretos.", "error");

  e.target.reset();
  entrar(usuario);
});

// ---------- Sair ----------
document.getElementById("logout-btn").addEventListener("click", () => {
  salvarSessao(null);
  mostrar("login");
});

// ---------- Restaurar sessão ----------
const emailSessao = lerSessao();
const logado = emailSessao && lerUsuarios().find(u => u.email === emailSessao);
if (logado) entrar(logado);
