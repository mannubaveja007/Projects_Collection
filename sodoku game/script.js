document.addEventListener('DOMContentLoaded', () => {
    // --- DOM Elements ---
    const boardElement = document.getElementById('sudoku-board');
    const newGameBtn = document.getElementById('new-game-btn');
    const checkSolutionBtn = document.getElementById('check-solution-btn');
    const resetBtn = document.getElementById('reset-btn');
    const hintBtn = document.getElementById('hint-btn');
    const difficultySelect = document.getElementById('difficulty');
    const themeSwitch = document.getElementById('theme-switch');
    const timerElement = document.getElementById('timer');
    const statsElements = {
        solved: document.getElementById('puzzles-solved'),
        time: document.getElementById('fastest-time'),
        totalTime: document.getElementById('total-time'),
    };
    const resetStatsBtn = document.getElementById('reset-stats-btn');
    const resetModal = document.getElementById('reset-modal');
    const confirmResetBtn = document.getElementById('confirm-reset-btn');
    const cancelResetBtn = document.getElementById('cancel-reset-btn');
    const successModal = document.getElementById('success-modal');
    const closeSuccessBtn = document.getElementById('close-success-btn');

    // --- Game State ---
    let board = [];
    let solution = [];
    let timerInterval;
    let seconds = 0;
    let stats = {
        puzzlesSolved: 0,
        fastestTime: null,
        totalTime: 0,
    };
    const difficulties = {
        easy: 45,
        medium: 35,
        hard: 25,
    };

    // --- Sudoku Logic ---

    function isSafe(grid, row, col, num) {
        for (let x = 0; x < 9; x++) {
            if (grid[row][x] === num || grid[x][col] === num) {
                return false;
            }
        }
        const startRow = row - (row % 3);
        const startCol = col - (col % 3);
        for (let i = 0; i < 3; i++) {
            for (let j = 0; j < 3; j++) {
                if (grid[i + startRow][j + startCol] === num) {
                    return false;
                }
            }
        }
        return true;
    };

    function solveSudoku(grid) {
        for (let row = 0; row < 9; row++) {
            for (let col = 0; col < 9; col++) {
                if (grid[row][col] === 0) {
                    for (let num = 1; num <= 9; num++) {
                        if (isSafe(grid, row, col, num)) {
                            grid[row][col] = num;
                            if (solveSudoku(grid)) {
                                return true;
                            }
                            grid[row][col] = 0;
                        }
                    }
                    return false;
                }
            }
        }
        return true;
    };

    function generatePuzzle() {
        let newBoard = Array(9).fill(0).map(() => Array(9).fill(0));
        fillBox(newBoard, 0, 0);
        fillBox(newBoard, 3, 3);
        fillBox(newBoard, 6, 6);
        solveSudoku(newBoard);
        solution = JSON.parse(JSON.stringify(newBoard));
        let cellsToRemove = 81 - difficulties[difficultySelect.value];
        while (cellsToRemove > 0) {
            let row = Math.floor(Math.random() * 9);
            let col = Math.floor(Math.random() * 9);
            if (newBoard[row][col] !== 0) {
                newBoard[row][col] = 0;
                cellsToRemove--;
            }
        }
        board = newBoard;
    };
    
    function fillBox(grid, row, col) {
        let nums = [1, 2, 3, 4, 5, 6, 7, 8, 9];
        for (let i = 0; i < 3; i++) {
            for (let j = 0; j < 3; j++) {
                let index = Math.floor(Math.random() * nums.length);
                let num = nums.splice(index, 1)[0];
                grid[row + i][col + j] = num;
            }
        }
    };

    // --- UI and Board Rendering ---
// REPLACE the old renderBoard function with this one
function renderBoard() {
    boardElement.innerHTML = '';
    for (let i = 0; i < 9; i++) {
        for (let j = 0; j < 9; j++) {
            const cell = document.createElement('div');
            cell.classList.add('cell');
            cell.dataset.row = i;
            cell.dataset.col = j;

            // Add classes for the thicker 3x3 grid borders
            if ((j + 1) % 3 === 0 && j < 8) {
                cell.classList.add('border-right');
            }
            if ((i + 1) % 3 === 0 && i < 8) {
                cell.classList.add('border-bottom');
            }

            if (board[i][j] !== 0) {
                cell.textContent = board[i][j];
                cell.classList.add('pre-filled');
            } else {
                const input = document.createElement('input');
                input.type = 'number';
                input.min = 1;
                input.max = 9;
                input.addEventListener('input', handleCellInput);
                input.addEventListener('keydown', handleCellKeyDown);
                cell.appendChild(input);
            }
            // Append the cell directly to the board element
            boardElement.appendChild(cell);
        }
    }
};

    // --- Event Handlers ---

    function handleCellInput(e) {
        let value = parseInt(e.target.value, 10);
        if (isNaN(value) || value < 1 || value > 9) {
            e.target.value = '';
            return;
        }
        if (e.target.value.length > 1) {
            e.target.value = e.target.value.slice(0, 1);
        }
        validateCell(e.target);
    }

    function handleCellKeyDown(e) {
        const cell = e.target.parentElement;
        const row = parseInt(cell.dataset.row);
        const col = parseInt(cell.dataset.col);

        let nextCell;
        switch (e.key) {
            case 'ArrowUp':
                nextCell = document.querySelector(`.cell[data-row="${row - 1}"][data-col="${col}"] input`);
                break;
            case 'ArrowDown':
                nextCell = document.querySelector(`.cell[data-row="${row + 1}"][data-col="${col}"] input`);
                break;
            case 'ArrowLeft':
                nextCell = document.querySelector(`.cell[data-row="${row}"][data-col="${col - 1}"] input`);
                break;
            case 'ArrowRight':
                nextCell = document.querySelector(`.cell[data-row="${row}"][data-col="${col + 1}"] input`);
                break;
        }
        if (nextCell) {
            e.preventDefault();
            nextCell.focus();
        }
    }
    
    function validateCell(inputElement) {
        clearErrors();
        const cell = inputElement.parentElement;
        const row = parseInt(cell.dataset.row);
        const col = parseInt(cell.dataset.col);
        const value = parseInt(inputElement.value);

        if (!value) return;

        for (let i = 0; i < 9; i++) {
            if (i !== col) {
                const peer = document.querySelector(`.cell[data-row="${row}"][data-col="${i}"]`);
                if ((peer.textContent || peer.querySelector('input')?.value) == value) {
                    cell.classList.add('error');
                    peer.classList.add('error');
                }
            }
            if (i !== row) {
                const peer = document.querySelector(`.cell[data-row="${i}"][data-col="${col}"]`);
                 if ((peer.textContent || peer.querySelector('input')?.value) == value) {
                    cell.classList.add('error');
                    peer.classList.add('error');
                }
            }
        }
        
        const startRow = row - row % 3;
        const startCol = col - col % 3;
        for (let i = 0; i < 3; i++) {
            for (let j = 0; j < 3; j++) {
                if ((startRow + i !== row) || (startCol + j !== col)) {
                   const peer = document.querySelector(`.cell[data-row="${startRow + i}"][data-col="${startCol + j}"]`);
                   if ((peer.textContent || peer.querySelector('input')?.value) == value) {
                        cell.classList.add('error');
                        peer.classList.add('error');
                    }
                }
            }
        }
    };

    // --- Game Functions ---
    
    function startNewGame() {
        clearErrors();
        generatePuzzle();
        renderBoard();
        startTimer();
    };

    function resetBoard() {
        clearErrors();
        const inputs = document.querySelectorAll('#sudoku-board input');
        inputs.forEach(input => input.value = '');
    };

    function checkSolution() {
        clearErrors();
        let isCorrect = true;
        let isComplete = true;

        for (let i = 0; i < 9; i++) {
            for (let j = 0; j < 9; j++) {
                const cell = document.querySelector(`.cell[data-row="${i}"][data-col="${j}"]`);
                let value;
                if (cell.classList.contains('pre-filled')) {
                    value = parseInt(cell.textContent);
                } else {
                    const input = cell.querySelector('input');
                    if (!input.value) {
                        isComplete = false;
                        continue;
                    }
                    value = parseInt(input.value);
                }

                if (value !== solution[i][j]) {
                    isCorrect = false;
                    cell.classList.add('error');
                }
            }
        }
        
        if (!isComplete) {
            alert("The board is not completely filled yet!");
            return;
        }

        if (isCorrect) {
            stopTimer();
            successModal.style.display = 'block';
            updateStatsOnCompletion();
        } else {
            alert("There are some errors. Keep trying!");
        }
    };
    
    function getHint() {
        const emptyCells = [];
        for (let i = 0; i < 9; i++) {
            for (let j = 0; j < 9; j++) {
                const cell = document.querySelector(`.cell[data-row="${i}"][data-col="${j}"]`);
                if (!cell.classList.contains('pre-filled') && !cell.querySelector('input').value) {
                    emptyCells.push({row: i, col: j});
                }
            }
        }

        if (emptyCells.length > 0) {
            const randomCell = emptyCells[Math.floor(Math.random() * emptyCells.length)];
            const { row, col } = randomCell;
            const hintCell = document.querySelector(`.cell[data-row="${row}"][data-col="${col}"]`);
            hintCell.querySelector('input').value = solution[row][col];
            hintCell.classList.add('hint');
            setTimeout(() => hintCell.classList.remove('hint'), 1000);
        } else {
            alert("No empty cells left to give a hint!");
        }
    };

    function clearErrors() {
        document.querySelectorAll('.cell.error').forEach(cell => cell.classList.remove('error'));
    };
    
    // --- Timer and Stats ---

    function startTimer() {
        stopTimer();
        seconds = 0;
        updateTimerDisplay();
        timerInterval = setInterval(() => {
            seconds++;
            stats.totalTime++;
            updateTimerDisplay();
        }, 1000);
    };

    function stopTimer() {
        clearInterval(timerInterval);
    };

    function updateTimerDisplay() {
        const minutes = Math.floor(seconds / 60);
        const remainingSeconds = seconds % 60;
        timerElement.textContent = `Time: ${String(minutes).padStart(2, '0')}:${String(remainingSeconds).padStart(2, '0')}`;
    };

    function loadStats() {
        const savedStats = localStorage.getItem('sudokuStats');
        if (savedStats) {
            stats = JSON.parse(savedStats);
        }
    };

    function saveStats() {
        localStorage.setItem('sudokuStats', JSON.stringify(stats));
    };

    function updateStatsDisplay() {
        statsElements.solved.textContent = stats.puzzlesSolved;
        statsElements.time.textContent = stats.fastestTime ? `${stats.fastestTime}s` : 'N/A';
        const totalMinutes = Math.floor(stats.totalTime / 60);
        const totalSeconds = stats.totalTime % 60;
        statsElements.totalTime.textContent = `${totalMinutes}m ${totalSeconds}s`;
    };

    function updateStatsOnCompletion() {
        stats.puzzlesSolved++;
        if (difficultySelect.value === 'medium') {
             if (stats.fastestTime === null || seconds < stats.fastestTime) {
                stats.fastestTime = seconds;
            }
        }
        saveStats();
        updateStatsDisplay();
    };

    // --- Attach Event Listeners ---
    newGameBtn.addEventListener('click', startNewGame);
    checkSolutionBtn.addEventListener('click', checkSolution);
    resetBtn.addEventListener('click', () => { resetModal.style.display = 'block'; });
    confirmResetBtn.addEventListener('click', () => { resetBoard(); resetModal.style.display = 'none'; });
    cancelResetBtn.addEventListener('click', () => { resetModal.style.display = 'none'; });
    closeSuccessBtn.addEventListener('click', () => { successModal.style.display = 'none'; });
    hintBtn.addEventListener('click', getHint);
    themeSwitch.addEventListener('change', () => { document.body.classList.toggle('dark-mode'); });
    resetStatsBtn.addEventListener('click', () => {
        if (confirm("Are you sure you want to reset all your stats permanently?")) {
            stats = { puzzlesSolved: 0, fastestTime: null, totalTime: 0 };
            saveStats();
            updateStatsDisplay();
        }
    });

    // --- Initialization ---
    function init() {
        loadStats();
        updateStatsDisplay();
        startNewGame();
    };

    init();
});