
import javax.swing.*;
public class guessGame {
    public static void main(String[] args) {

      int  numbers = (int) (Math.random() * 10 + 1);
      int guessed = 0;
      System.out.println("Guess a number between 1 and 10: ");
      int count = 1;

      while(guessed != numbers){
        String response = JOptionPane.showInputDialog(null, "Enter a number between 1 and 10: ", "Guess a number", 3); // null is the parent component, 3 is the message type
        guessed = Integer.parseInt(response);
        JOptionPane.showMessageDialog(null,"" + determineGuess(guessed, numbers, count) );
        count ++;
      }
    }
      public static String determineGuess(int guessed, int numbers, int count){
        if (guessed <= 0 || guessed > 10){
          return "You must enter a number between 1 and 10";
        }
        else if (guessed == numbers){
          return "You guessed it! It took you " + count + " tries.";
        }
        else if (guessed < numbers){
          return "You guessed too low.\n Try number:"  + count;
        }
        else if (guessed > numbers){
          return "You guessed too high.\n Try number: " + count;
        }
        else{
          return "You guesses is not correctly.\n Try number: " + count;
        }
      }
    }  
