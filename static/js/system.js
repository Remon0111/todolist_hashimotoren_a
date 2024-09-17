
$(function() {
    $('body').terminal({
        help : function() {
            this.echo("==================================================\n What would you like to do?\n==================================================\n1. Add Todo\n2. View Todos\n3. Update Todo\n4. Calendar Todo\n5. reporting Todo\n6. Delete Todo\n7. Exit\n==================================================");
        },
        add : async function() {
            const tasklist = [];
            await this.read('[[;#00bfff;]Enter the task: ', EnterTask => {tasklist.push(EnterTask)});
            await this.read("[[;#00bfff;]Please enter the year for the task: ", YearTask => {tasklist.push(YearTask)});
            await this.read("[[;#00bfff;]Please enter the month for the task: ", MonthTask => {tasklist.push(MonthTask)});
            await this.read("[[;#00bfff;]Please enter the day for the task: ", DayTask => {tasklist.push(DayTask)});
            await this.read("[[;#00bfff;]Please enter the Hour for the task: ", HourTask => {tasklist.push(HourTask)});
            if (tasklist[0] == "") {
                this.echo("No tasks entered");
            }else {
                if (tasklist[1] == "" || tasklist[2] == "" || tasklist[3] == "" || tasklist[4] == "") {
                    const Entered = [];
                    await this.read("Is it okay if I leave out some items?(yes/no): ", notEntered => {Entered.push(notEntered)});
                    if (Entered[0] == "yes" || Entered[0] == "Yes") {
                        const formData = new FormData();
                        formData.append('todoName', tasklist[0]);
                        formData.append('todoYear', tasklist[1]);
                        formData.append('todoMonth', tasklist[2]);
                        formData.append('todoDay', tasklist[3]);
                        formData.append('todoHour', tasklist[4]);
                        fetch('/process', {
                            method: 'POST',
                            body: formData //入力値を入れたリストを参照
                        })
                        await this.echo("[[;#32cd32;]\nTodo added successfully!\n");
                    }else {
                        await this.echo("Input failure");
                    }
                }else {
                    const formData = new FormData();
                    formData.append('todoName', tasklist[0]);
                    formData.append('todoYear', tasklist[1]);
                    formData.append('todoMonth', tasklist[2]);
                    formData.append('todoDay', tasklist[3]);
                    formData.append('todoHour', tasklist[4]);
                    fetch('/process', {
                        method: 'POST',
                        body: formData
                    })
                    await this.echo("[[;#32cd32;]\nTodo added successfully!\n");
                }
            }
        },
        view : function() {
            const viewTask = [];
            fetch('/send-list' ,{
                method: 'GET',
            })
            .then(response => response.json())
            .then(data => {
                // 受け取ったリストを使用して何か処理を行う
                console.log(data.list);
                viewTask.push(data.list);
                this.echo("[[;#32cd32;]Your Todos:")
                this.echo("[[;#32cd32;]--------------------------------------------------")
                for (const task of data.list) {
                    this.echo(task[0] + ". " + task[6] + "|" + task[2] + "/" + task[3] + "/" + task[4] + "/" + task[5] + ": " + task[1]);
                }
                this.echo("[[;#32cd32;]--------------------------------------------------")
            })
            .catch((error) => {
                console.error('Error:', error);
            });
            this.echo(viewTask)
        },
        update : function() {
            const updateViewTask = [];
            fetch('/send-list' ,{
                method: 'GET',
            })
            .then(response => response.json())
            .then(async data => {
                // 受け取ったリストを使用して何か処理を行う
                console.log(data.list);
                updateViewTask.push(data.list);
                for (const task of data.list) {
                    this.echo(task[0] + ". " + task[7] + "|" + task[3] + "/" + task[4] + "/" + task[5] + "/" + task[6] + ": " + task[2]);
                };
                const updateTaskNumber = []
                const updateChange = []
                await this.read("Please select the task number: ", updateNumber => {updateTaskNumber.push(updateNumber)});
                await this.read("Please select what you want to change: ", updateTaskChange => {updateChange.push(updateTaskChange)});
                if (updateChange[0] == "task") {
                    updateTaskNumber.push("taskName");
                    await this.read("Enter the new task: ", updateTaskName => {updateTaskNumber.push(updateTaskName)});
                    const formData = new FormData();
                    formData.append('updateTaskNumber', updateTaskNumber[0]);
                    formData.append('updateTaskContent', updateTaskNumber[1]);
                    formData.append('updateTaskInput', updateTaskNumber[2]);
                    fetch('/update_todo', {
                        method: 'POST',
                        body: formData
                    })
                    await this.echo("[[;#32cd32;]\nTodo added successfully!\n");
                }else if (updateChange[0] == "taskYear") {
                    updateTaskNumber.push("taskYear");
                    await this.read("Enter the new task: ", updateTaskYear => {updateTaskNumber.push(updateTaskYear)});
                    const formData = new FormData();
                    formData.append('updateTaskNumber', updateTaskNumber[0]);
                    formData.append('updateTaskContent', updateTaskNumber[1]);
                    formData.append('updateTaskInput', updateTaskNumber[2]);
                    fetch('/update_todo', {
                        method: 'POST',
                        body: formData
                    })
                    await this.echo("[[;#32cd32;]\nTodo added successfully!\n");
                }else if (updateChange[0] == "taskMonth") {
                    updateTaskNumber.push("taskMonth");
                    await this.read("Enter the new task: ", updateTaskMonth => {updateTaskNumber.push(updateTaskMonth)});
                    const formData = new FormData();
                    formData.append('updateTaskNumber', updateTaskNumber[0]);
                    formData.append('updateTaskContent', updateTaskNumber[1]);
                    formData.append('updateTaskInput', updateTaskNumber[2]);
                    fetch('/update_todo', {
                        method: 'POST',
                        body: formData
                    })
                    this.echo("[[;#32cd32;]\nTodo added successfully!\n");
                }else if (updateChange[0] == "taskDay") {
                    updateTaskNumber.push("taskDay");
                    await this.read("Enter the new task: ", updateTaskDay => {updateTaskNumber.push(updateTaskDay)});
                    const formData = new FormData();
                    formData.append('updateTaskNumber', updateTaskNumber[0]);
                    formData.append('updateTaskContent', updateTaskNumber[1]);
                    formData.append('updateTaskInput', updateTaskNumber[2]);
                    fetch('/update_todo', {
                        method: 'POST',
                        body: formData
                    })
                    await this.echo("[[;#32cd32;]\nTodo added successfully!\n");
                }else if (updateChange[0] == "taskHour") {
                    updateTaskNumber.push("taskHour");
                    await this.read("Enter the new task: ", updateTaskHour => {updateTaskNumber.push(updateTaskHour)});
                    const formData = new FormData();
                    formData.append('updateTaskNumber', updateTaskNumber[0]);
                    formData.append('updateTaskContent', updateTaskNumber[1]);
                    formData.append('updateTaskInput', updateTaskNumber[2]);
                    fetch('/update_todo', {
                        method: 'POST',
                        body: formData
                    })
                    await this.echo("[[;#32cd32;]\nTodo added successfully!\n");
                }else {
                    this.echo("The information you entered is not an option");
                };
            })
            .catch((error) => {
                console.error('Error:', error);
            });
        },
        reporting : async function() {
            const updateViewTask = [];
            fetch('/send-list' ,{
                method: 'GET',
            })
            .then(response => response.json())
            .then(async data => {
                // 受け取ったリストを使用して何か処理を行う
                console.log(data.list);
                updateViewTask.push(data.list);
                for (const task of data.list) {
                    this.echo(task[0] + ". " + task[7] + "|" + task[3] + "/" + task[4] + "/" + task[5] + "/" + task[6] + ": " + task[2]);
                };
                const reportinglist = [];
                await this.read("Please enter the number of the task you are reporting: ", ReportingNumber =>{reportinglist.push(ReportingNumber)});
                await this.read("Is it done? (yes/no): ", Reportingdone =>{reportinglist.push(Reportingdone)});
                if (reportinglist[1] == "yes") {
                    await this.read("Are you sure you want to change it(yes/no): ", ReportingDone =>{reportinglist.push(ReportingDone)});
                    if (reportinglist[2] == "yes") {
                        reportinglist.push("○")
                        const formData = new FormData();
                        formData.append('reportingNumber', reportinglist[0]);
                        formData.append('reportingMark', reportinglist[3]);
                        fetch('/reporting_todo', {
                            method: 'POST',
                            body: formData
                        })
                        await this.echo("[[;#32cd32;]\nTodo added successfully!\n");
                    }else if (reportinglist[2] == "no") {
                        await this.echo("Input failed")
                    }
                }else if (reportinglist[1] == "no") {
                    await this.read("Are you sure you want to change it(yes/no): ", ReportingDone =>{reportinglist.push(ReportingDone)});
                    if (reportinglist[2] == "yes") {
                        reportinglist.push("×")
                        const formData = new FormData();
                        formData.append('reportingNumber', reportinglist[0]);
                        formData.append('reportingMark', reportinglist[3]);
                        fetch('/reporting_todo', {
                            method: 'POST',
                            body: formData
                        })
                        await this.echo("[[;#32cd32;]\nTodo added successfully!\n");
                    }else if (reportinglist[2] == "no") {
                        await this.echo("Input failed")
                    }
                }
            });
        },
        delete : async function() {
            const updateViewTask = [];
            fetch('/send-list' ,{
                method: 'GET',
            })
            .then(response => response.json())
            .then(async data => {
                // 受け取ったリストを使用して何か処理を行う
                console.log(data.list);
                updateViewTask.push(data.list);
                for (const task of data.list) {
                    this.echo(task[0] + ". " + task[6] + "|" + task[2] + "/" + task[3] + "/" + task[4] + "/" + task[5] + ": " + task[1]);
                };
                const deleteList = [];
                await this.read("Enter the number of the todo to delete: ", deletetodo =>{deleteList.push(deletetodo)});
                await this.read("Are you sure you want to change it(yes/no): ", deleteDone =>{deleteList.push(deleteDone)});
                if (deleteList[1] == "yes") {
                    const formData = new FormData();
                    formData.append('deleteNumber', deleteList[0]);
                    fetch('/delete_todo', {
                        method: 'POST',
                        body: formData
                    })
                    await this.echo("[[;#32cd32;]\nTodo added successfully!\n");
                }else if (deleteList[1] == "no") {
                    await this.echo("Input failed")
                }else {
                    await this.echo("Input failed")
                }
            })
        },
        setting : async function() {
            this.echo("==================================================\n1. Languages\n2. fontsize\n3. account\n==================================================")
            await this.echo()
        },
        exit : async function() {
            await this.echo("[[;#00bfff;]==================================================\n")
            await this.echo("[[;#32cd32;]  ____                 _ _                _ \n / ___| ___   ___   __| | |__  _   _  ___| |\n| |  _ / _ \\ / _ \\ / _` | '_ \\| | | |/ _ \\ |\n| |_| | (_) | (_) | (_| | |_) | |_| |  __/_|\n \\____|\\___/ \\___/ \\__,_|_.__/ \\__, |\\___(_)\n                               |___/        ")
            await this.echo("[[;#00bfff;]\n\n==================================================")
        }
    },{
        greetings: opening.innerHTML
    });
    db.close();
});

db.close();