 // API response is of the form:
 //
 //     {'quantity':{0:2, 1:1},
 //      'correct': {0:1, 1:0},
 //      'grades': {0:.92, 1:.5},
 //      'graded': False,
 //      'problems': [
 //          {'question': '', 'answer':'', 'difficulty': 0, 'result':True},
 //          {'question': '', 'answer':'', 'difficulty': 0, 'result':False},
 //          {'question': '', 'answer':'', 'difficulty': 1, 'result':False}
 //          ],
 //      }


fetchProblemSet() {
  fetch("http://localhost:5000/api/problem_set_generator/10/2")
    .then(response => response.json())
    .then((data) => {this.setState({
      problem_set: data,
      question: data['problems'][this.counter]['question'],
      correct_answer: data['problems'][this.counter]['answer']
    })})
    .catch(error => {
      console.log(error);
      this.setState({
        error: error
      })
    });
}
