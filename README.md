<h1>BirdClassifier_Pytorch_Side_Project</h1>

<h2>Contibuters</h2>
<ul>
  <li><b>Ayush Dhanai</b> - Slack Id : <i>@Ayush Dhanai</i></li>
  <li><b>Akhil Tiwari</b> &nbsp &nbsp- Slack Id : <i>@Akhil_Tiwari</i></li>
</ul>

<h2>Architecture and details of the model</h2>
<ul>
  <li><b>Pre-Trained Model used :</b> Densenet121</li>
  <li><b>Dataset Used :</b> <a href="http://www.vision.caltech.edu/visipedia/CUB-200.html">Caltech-UCSD Birds 200</a></li>
  <li><b>Accuracy Achieved :</b> 94.5% </li>
  <li><b>Optimizer Used :</b> ADAM</li>
  <li><b>Loss Function :</b> NLLLoss</li>
  <li><b>Learning Rate Scheduler :</b> StepLR</li>
</ul>
<h2>Libraries and Frameworks Used </h2>
<ul>
  <li><b>Deep Learning Framework used :</b><a href="https://pytorch.org/"> PyTorch</a></li>
  <li><b>Deployed On :</b> <a href="https://www.heroku.com/">Heroku</a></li>
</ul>
<h2>Dependencies </h2>
<ol>
   <li><a href="http://flask.pocoo.org/">Flask</a></li>
   <li><a href="https://pytorch.org/">torch and torchvision</a></li>
   <li><a href="http://www.numpy.org/">numpy</a></li>
   <li><a href="https://pypi.org/project/Pillow/">Pillow</a></li>
   <li><a href="https://pypi.org/project/wikipedia/">wikipedia</a></li>
</ol>
<h2>Running this project</h2>
<ol>
  <li>Clone or download the repository on your local machine</li>
  <li>Make sure all the dependencies are installed</li>
  <li>open the teminal and change current working directory to project directory</li>
  <li>set the value of FLASK_APP environment variable to "application.py"</li>
  <li>run command "flask run" inside the terminal</li>
</ol>
<h2><b>About the project - <b></h2><h4>Creating a web application with the help of convolutional neural networks and transfer learning, that can be used to detect the species of the bird from its image. Application can be proved useful in the field of Ornithology (branch of zoology concern with the study of birds) and can also be used by people interested in wildlife photography.</h4>

<h2>&nbsp;&nbsp;<b>Screenshots of working application</b></h2><br/>
  <h3>&nbsp;&nbsp;<b>Homepage -</b>upload the image from your device into the application and then model will predict &nbsp;&nbsp;the species of the bird and display information regarding that particular species.</h3>
<img src="/static/homepage.jpg"/><br/><br/>
  <h3>&nbsp;&nbsp;<b>Displaying result</b></h3>
<img src="/static/result_page.jpg"/>


<h4>&nbsp;&nbsp;Let us know if any issue arise and we'd love your contribution in making this project even better.</h4>
