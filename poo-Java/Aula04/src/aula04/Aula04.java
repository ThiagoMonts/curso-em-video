package aula04;
public class Aula04 {
    public static void main(String[] args) {
        Caneta c1 = new Caneta("NIC", "Amarelo", 0.4f);
        c1.status();
        
        Caneta c2 = new Caneta("kkk", "laranja", 1.5f);
        c2.status();
        
        
        
        
        
        
        /*c1.setModelo("BIC");
        c1.modelo = "BIC"; //Posso usar qualquer uma das opções, pois esse acesso é público
        
        c1.setPonta(0.5f);
        //c1.ponta = 0.5f; //Não consigo utilizar esse método, pois o acesso é privado
        
        //c1.status();
        System.out.println("Tenho uma caneta " + c1.getModelo()); //Tanto posso usar o c1.modelo, quanto o c1.getModelo()
        */
    }
    
}