import axios from 'axios';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';

// axios.defaults.baseURL = 'http://localhost:3000';
// axios.defaults.headers.post['Content-Type'] = 'application/json;charset=utf-8';
axios.defaults.headers.post['Access-Control-Allow-Origin'] = '*';


function post(title=null, description=null, start_date=null, start_time=null, end_date=null, end_time=null) {

    const data = {
        'title': title,
        'description': description,
        'start_date': start_date,
        'start_time': start_time,
        'end_date': end_date,
        'end_time': end_time
    };
  
    axios.get('https://croissant.pythonanywhere.com/layers/')

        .then(res => {
            console.log('e')
            console.log("ステータスコード:", res);
        })

        .catch(err => {
            console.log("err:", err);
        });
    console.log('test');
  
    axios.post('https://croissant.pythonanywhere.com/layers/', data)
  
        .then(res => {
            console.log(res);
        })
        
        .catch(err => {
            console.log('err:', err);
        });
}


export default function Home() {
    return (
        <div>
            <h1 className="text-3xl font-bold underline">
                Hello world!
            </h1>
            <TextField id="title" label="Title" variant="outlined" />
            <TextField id="description" label="Description" variant="outlined" multiline rows="3" />
            <p>start date</p>
            <input type="date" id="start-date"></input>
            <p>start time</p>
            <input type="time" id="start-time"></input>
            <p>end date</p>
            <input type="date" id="end-date"></input>
            <p>end time</p>
            <input type="time" id="end-time"></input>
            <Button variant="contained" onClick={() => post(
            // title=document.getElementById('title').value,
            // description=document.getElementById('description').value,
            // start_date=document.getElementById('start-date').value,
            // start_time=document.getElementById('start-time').value,
            // end_date=document.getElementById('end-date').value,
            // end_time=document.getElementById('end-time').value
            )}>Create</Button>
      </div>
    )
}
