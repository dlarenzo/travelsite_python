# https://www.wix.com/website-template/view/html/1845

from website import create_app


app = create_app()

if __name__ == '__main__':
  app.run(debug=True)