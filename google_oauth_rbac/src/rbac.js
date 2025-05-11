export function getUserRole(email) {
  if (email.endsWith('@ufjf.br')) {
    return 'Teacher';
  } else if (email.endsWith('@estudante.ufjf.br')) {
    return 'Student';
  } else {
    return 'Guest';
  }
}