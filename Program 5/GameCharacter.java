
public class GameCharacter{
    private String name;
    private int lives;
    private String[] inventory;
    private final int MAXLIVES = 5;
    
    public GameCharacter(){
        this.name = "Sam Sung";
        this.lives = MAXLIVES;
        this.inventory = new String[5];
    }

    public String getName(){
        return name;
    }
    public void setName(String newName){
        this.name = newName;
    }
    public int getLives(){
        return lives;
    }
    public void setLives(int num){
        if(0 <= num && num <= MAXLIVES){
            this.lives = num;
        }
    }

    public boolean isAlive(){
        return this.lives > 0;
    }
    public boolean hasWeapon(){
        for (String weapon: this.inventory){
            if(weapon == "knife" || weapon == "gun"){
                return true;
            }   
        }
        return false;
    }

    public int sizeOfInventory(){
        int num = 0;
        for (int i=0; i<5; i++){
            if(inventory[i] != null){
                num++;
            }
        }
        return num;
    }

    public void heal(){
        this.lives = MAXLIVES;
    }

    public void damage(){
        if(isAlive()){
            this.lives -= 1;
        }
    }

    public void pickUp(String item){
        for(int i=0;i<5;i++){
            if(this.inventory[i] == null){
                this.inventory[i] = item;
                break;
            }
        }
    }

    public void drop(String item){
        for(int i=0;i<5;i++){
            if(this.inventory[i] == item){
                this.inventory[i] = null;
                break;
            }
        }
    }

    public String toString(){
        String str = "Name:\t" + this.name + "\nLives:\t" + this.lives + "Inventory:\t";
        for(int i=0;i<5;i++){
            if(this.inventory[i] == null){
                str += inventory[i];
            }
        }
        return str;
    }
}