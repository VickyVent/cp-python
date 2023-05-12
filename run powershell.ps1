# Caminho dos arquivos Python (relativo ao local em que o script é executado)
$bubblesort_script = ".\bubblesort.py"
$mergesort_script = ".\mergesort.py"
$quicksort_script = ".\quicksort.py"

# Executar o primeiro arquivo Python e capturar o tempo de execução
$bubblesort_script_output = python $bubblesort_script 2>&1 | Out-String
$bubblesort_script_runtime = ($bubblesort_scriptoutput -split "`n" | Where-Object { $ -match "O programa levou" }) -replace "^[!] "

# Exibir o tempo de execução do primeiro arquivo Python
Write-Host "Tempo de execução do bubblesort.py: $bubblesort_script_runtime"

# Esperar 5 segundos
Start-Sleep -Seconds 5

# Executar o segundo arquivo Python e capturar o tempo de execução
$mergesort_script_output = python $mergesort_script 2>&1 | Out-String
$mergesort_script_runtime = ($mergesort_scriptoutput -split "`n" | Where-Object { $ -match "O programa levou" }) -replace "^[!] "

# Exibir o tempo de execução do segundo arquivo Python
Write-Host "Tempo de execução do mergesort.py: $mergesort_script_runtime"

# Esperar 5 segundos
Start-Sleep -Seconds 5

# Executar o terceiro arquivo Python e capturar o tempo de execução
$quicksort_script_output = python $quicksort_script 2>&1 | Out-String
$quicksort_script_runtime = ($quicksort_scriptoutput -split "`n" | Where-Object { $ -match "O programa levou" }) -replace "^[!] "

# Exibir o tempo de execução do terceiro arquivo Python
Write-Host "Tempo de execução do quicksort.py: $quicksort_script_runtime"