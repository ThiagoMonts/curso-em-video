package projetopessoas;
public class Aluno extends Pessoa{
    //Atributos
    private int matr;
    private String curso;
    
    //M�todos
    public void cancelarMatr() {
        System.out.println("Matr�cula ser� cancelada!");
    }
    
    //M�todos Especiais
    public int getMatr() {
        return matr;
    }

    public void setMatr(int matr) {
        this.matr = matr;
    }

    public String getCurso() {
        return curso;
    }

    public void setCurso(String curso) {
        this.curso = curso;
    }
    
}
