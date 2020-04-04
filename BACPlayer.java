import java.util.*;

public interface BACPlayer {

    /**
     * Returns the author of the agent.
     * @return The author as a string of form "Lastname, Firstname".
     */
    public String getAuthor();
    
    /**
     * Returns the student ID of the author of this agent.
     * @return The author's student ID as a string.
     */
    public String getStudentID();
    
    /**
     * This method is called exactly once by the {@code BACRunner} engine in the beginning. 
     * Inside this method, you should initialize whatever internal data structures you use
     * to store the list of possible words to speed up your future computations.
     */
    public void initializeWordList(List<String> words);
    
    /**
     * Given the current state of the game, return the next guess by the player agent.
     * @param n The length of the secret word.
     * @param guesses List of guesses done so far. Empty list, if no guesses have been made.
     * @param bulls List of number of bulls that each guess in {@code guesses} contained.
     * @param cows List of number of cows that each guess in {@code guesses} contained.
     * @return The word chosen by this agent as the next guess.
     */
    public String guess(int n, List<String> guesses, List<Integer> bulls, List<Integer> cows);
    
}