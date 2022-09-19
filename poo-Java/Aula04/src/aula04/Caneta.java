package aula04;
public class Caneta { //Atalho para criar o construtor, getters e setters Alt + Insert
    public String modelo;
    private float ponta;
    private String cor;
    private boolean tampada;
    
    public Caneta(String m, String c, float p){
        this.modelo = m;
        this.cor = c;
        this.ponta = p; //Também poderia fazer this.setPonta(p);
        this.tampar(); 
    } 
    
    
    /*public Caneta () { //O método construtor sempre terá o mesmo nome da classe
         this.tampar();
         this.cor = "Azul";
     }*/
    
    public String getModelo() {
        return this.modelo;
    }
    public void setModelo(String m) {
        this.modelo = m;
    }
    
    public float getPonta(){
        return this.ponta;
    }
    
    public void setPonta(float p) {
        this.ponta = p;
    }
    
    public void tampar() {
        this.tampada = true;
    }
    
    public void destampar() {
        this.tampada = false;
    }
    
    public void status() {
        System.out.println("SOBRE A CANETA:");
        System.out.println("Modelo: " + this.getModelo()); //Tanto posso usar o this.modelo, quanto o this.getModelo()
        System.out.println("Ponta: " + this.getPonta()); //Tanto posso usar o this.ponta, quanto o this.getPonta()
        System.out.println("Cor: " + this.cor);
        System.out.println("Tampada: " + this.tampada);
    }
    
    
}
