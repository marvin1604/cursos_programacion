class main{
    public static void main(String[] args) {
        System.out.println("hola Mundo");
        Car car = new Car("AMQ123", Account("andres herrera", "NAD234"));
        car.passenger= 4;
        // System.out.println("Car license:" + car.license );
        car.printDataCar();
        
    }
}