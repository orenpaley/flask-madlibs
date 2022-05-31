from flask import Flask, render_template, request

import stories

app = Flask(__name__)


@app.route("/")
def homeMad():
  return render_template(
    "/home.html", stories = stories.STORIES
  )


@app.route("/form")
def formMad():
    storyId = request.args.get('id', type=int)
    return render_template(
      "/form.html",
      words = stories.STORIES[storyId].getWords(), 
      len = len(stories.STORIES[storyId].getWords()),
      storyId = storyId
      )
      
@app.route('/story')
def getStory():
  answers = request.args
  storyId = request.args.get('storyId', type=int)
  return render_template(
    "/story.html",
    story = stories.STORIES[storyId].generate(answers))

  