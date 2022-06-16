# Do not modify these lines
__winc_id__ = "7b9401ad7f544be2a23321292dd61cb6"
__human_name__ = "arguments"

# Add your code after this line
def greet(name, greeting_template="Hello, <name>!"):
    return greeting_template.replace("<name>", name)


gravity_factor = {
    "sun": 274,
    "jupiter": 24.92,
    "neptune": 11.15,
    "saturn": 10.44,
    "earth": 9.798,
    "uranus": 8.87,
    "venus": 8.87,
    "mars": 3.71,
    "mercury": 3.7,
    "moon": 1.62,
    "pluto": 0.58,
}


def force(mass: float, body="earth"):
    if body.lower() in gravity_factor:
        return mass * round(gravity_factor[body.lower()], 1)

    return


def pull(m1, m2, d):
    G = 6.674 * 10**-11
    return G * ((m1 * m2) / d**2)


print(greet("Marco"))
print(greet("Bob", "What's up, <name>!"))

print(force(99))

print(pull(10, 101, 30))
