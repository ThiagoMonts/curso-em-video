package aula011;
public class Tecnico extends Aluno{
    private int registro;
    
    public void praticar(){
        System.out.println("Praticando o que foi aprendido.");
    }

    public int getRegistro() {
        return registro;
    }

    public void setRegistro(int registro) {
        this.registro = registro;
    }
    
}
