Sub UnMergeFill()

Dim cell As Range, joinedCells As Range

Application.ScreenUpdating = False
Application.Calculation = xlCalculationManual

For Each cell In ThisWorkbook.ActiveSheet.UsedRange
    If cell.MergeCells Then
        Set joinedCells = cell.MergeArea
        cell.MergeCells = False
        joinedCells.Value = cell.Value
    End If
Next

Application.ScreenUpdating = True
Application.Calculation = xlCalculationAutomatic

End Sub