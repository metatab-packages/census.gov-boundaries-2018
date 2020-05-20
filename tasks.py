from invoke import task

s3_bucket='library.metatab.org'
wp_site='data.sandiegodata.org'

@task
def build(c, force=False):
    c.run(f"mp build -r {'-F' if force else ''}")
   
@task
def s3(c):
    c.run(f"mp s3 -s {s3_bucket}")
   
    
@task
def publish(c):
    c.run(f"mp s3 -s {s3_bucket}")
    c.run(f"mp wp -s {wp_site} -p")