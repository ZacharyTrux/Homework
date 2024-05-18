/* name: Zachary Truxillo 
 * Date: 5/14/2024
 * Description: A simple java code to help learn syntax, 
 * it utilizes all major methods taught up to this point and is a simple character class
*/


public class GameCharacter{
    // Initialize all private variables (only variables the class can use)
    private String name;
    private int lives;
    // creates the inventory to be an array which is initially five unless given something different 
    private String[] inventory = new String[5];
    private final int MAXLIVES = 5;
    
    // Constructor which assigns a default name if the constructor is called 
    public GameCharacter(){
        this.name = "Sam Sung";
        this.lives = MAXLIVES;
    }

    // Overloaded Constructor
    public GameCharacter(String name, int lives){
        this.name = name;
        setLives(lives);
    }

    // Getters and setters for private variables
    public String getName(){
        return this.name;
    }
    public void setName(String newName){
        this.name = newName;
    }

    public int getLives(){
        return this.lives;
    }
    public void setLives(int num){
        if (0 <= num && num <= MAXLIVES){
            this.lives = num;
        }
        else{
            this.lives = MAXLIVES;
        }
    }

    public String[] getInventory(){
        return this.inventory;
    }
    public void setInventory(String[] array){
        {
            this.inventory = array;
        }
    }

    // Returns a true or false value
    public boolean isAlive(){
        return this.lives > 0;
    }

    // flag to check if character has any weapon items
    public boolean hasWeapon(){
        for (String weapon: this.inventory){
            if (weapon == "knife" || weapon == "gun"){
              return true;
            }
        }
        return false;
    }

    // iterate through the inventory returning spaces taken up by something other than null 
    public int sizeOfInventory(){
        int num = 0;
        for (int i = 0; i < this.inventory.length; i++){
            if (this.inventory[i] != null){
                num++;
            }
        }
        return num;
    }

    // account for the character restoring their health
    public void heal(){
        this.lives = MAXLIVES;
    }

    // account for the character being attacked 
    public void damage(){
        if (isAlive()){
            this.lives -= 1;
        }
    }

    // add items into the inventory to the first null(empty) spot found
    public void pickUp(String item){
        for (int i = 0; i < this.inventory.length; i++){
            if (this.inventory[i] == null){
                this.inventory[i] = item;
                break;
            }
        }
    }

    // gets rid of the given item from the inventory and makes the spot "open" or null again
    public void drop(String item){
        for (int i = 0; i < this.inventory.length; i++){
            if (this.inventory[i] == item){
                this.inventory[i] = null;
                break;
            }
        }
    }

    // returns a string which correctly formats all character information
    public String toString(){
        String str = "Name:\t" + this.name + "\nLives:\t" + this.lives + "\nInventory:\t";
        for (int i = 0; i < this.inventory.length; i++){
            if (this.inventory[i] != null){
                str += this.inventory[i]+", ";
            }
        }

        str += "\n";
        return str;
    }
}