public class SimulationRunner {
    public static void main(String[] args) {
        TTT3D game = new TTT3D();
        game.setVisible(false); // Disable GUI

        // Test all 27 starting moves with 100 games each
        for (int board = 0; board < 3; board++) {
            for (int row = 0; row < 3; row++) {
                for (int col = 0; col < 3; col++) {
                    game.simulateGamesForMove(board, row, col, 1000);
                }
            }
        }
        System.exit(0);
    }
}