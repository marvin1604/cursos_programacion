class UberX extends Car {
    String brand;
    String model;

    public UberX(String license, Account driver, String model, String brand){
        super(license, driver);
        this.brand = brand;
        this.model = model; 
        
    }
    
}
