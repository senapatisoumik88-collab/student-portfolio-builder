name = request.form.get("name")
skills = request.form.get("skills")
projects = request.form.get("projects")

photo = request.files.get("photo")

photo_filename = None

if photo and photo.filename != "":
    photo_filename = photo.filename
    photo.save(os.path.join(app.config["UPLOAD_FOLDER"], photo_filename))

return render_template(
    "portfolio.html",
    name=name,
    skills=skills,
    projects=projects,
    photo=photo_filename
)
