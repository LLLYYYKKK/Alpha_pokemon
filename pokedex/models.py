from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.deconstruct import deconstructible
# Create your models here.

class Name(models.Model):
    korean = models.CharField(max_length=20, default='이름 없음')
    english = models.CharField(max_length=20, default='No name')

    def __str__(self):
        return self.korean

class Description(models.Model):
    korean = models.CharField(max_length=200, default='설명 없음')
    english = models.CharField(max_length=200, default="No description")

    def __str__(self):
        return self.korean

class PokemonType(models.Model):
    name = models.OneToOneField(Name, on_delete=models.CASCADE)
    super_effective_types = models.ManyToManyField("self", blank=True, related_name='+', symmetrical=False)
    not_very_effective_types = models.ManyToManyField("self", blank=True, related_name='+', symmetrical=False)
    ineffective_types = models.ManyToManyField("self", blank=True, related_name='+', symmetrical=False)

    def __str__(self):
        return self.name.korean

class PokemonAbility(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.OneToOneField(Name, on_delete=models.CASCADE, null=True)
    description = models.OneToOneField(Description, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name.korean

class PokemonMoveCategory(models.Model):
    name = models.OneToOneField(Name, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name.korean

class MoveAffect(models.Model):
    name = models.OneToOneField(Name, on_delete=models.CASCADE, null=True)
    description = models.OneToOneField(Description, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name.korean

class SecondaryEffect(models.Model):
    name = models.OneToOneField(Name, on_delete=models.CASCADE, null=True)
    description = models.ForeignKey(Description, on_delete=models.CASCADE, null=True)
    accuracy = models.FloatField(default=1.0)

    def __str__(self):
        return self.name.korean

class PokemonMove(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.OneToOneField(Name, on_delete=models.CASCADE, null=True)
    type = models.ForeignKey(PokemonType, on_delete=models.CASCADE, null=True)
    description = models.OneToOneField(Description, on_delete=models.CASCADE, null=True)
    damage = models.IntegerField(default=60)
    accuracy = models.FloatField(default=1.0)
    pp = models.IntegerField(default=5)
    max_pp = models.IntegerField(default=10)
    category = models.ForeignKey(PokemonMoveCategory, on_delete=models.CASCADE, null=True)
    priority = models.IntegerField(default=0)
    is_contact = models.BooleanField(default=False)
    affect = models.ForeignKey(MoveAffect, on_delete=models.CASCADE, null=True)
    affected_by_magic_coat = models.BooleanField(default=True)
    affected_by_bright_powder = models.BooleanField(default=True)
    affected_by_protect = models.BooleanField(default=True)
    affected_by_snatch = models.BooleanField(default=True)
    affected_by_kings_rock = models.BooleanField(default=True)
    secondary_effect = models.ForeignKey(SecondaryEffect, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name.korean

    def pokemons_can_learn(self):
        return self.pokemonspec_set.order_by('index_number')

    def accuracy_to_str(self):
        if self.accuracy < 0:
            return '--'
        else:
            return str(self.accuracy_to_int()) + '%'

    def accuracy_to_int(self):
        return int(self.accuracy * 100)

    def damage_to_str(self):
        if self.damage < 0:
            return '--'
        else:
            return str(self.damage)

class PokemonSpec(models.Model):
    index_number = models.IntegerField(default=1)
    name = models.OneToOneField(Name, on_delete=models.CASCADE)
    base_hp = models.IntegerField(default=100)
    base_attack = models.IntegerField(default=100)
    base_defense = models.IntegerField(default=100)
    base_special_attack = models.IntegerField(default=100)
    base_special_defense = models.IntegerField(default=100)
    base_speed = models.IntegerField(default=100)
    types = models.ManyToManyField(PokemonType, blank=True)
    can_learn_moves = models.ManyToManyField(PokemonMove, blank=True)
    can_have_abilities = models.ManyToManyField(PokemonAbility, blank=True)
    hidden_ability = models.ManyToManyField(PokemonAbility, related_name='hidden_ability', blank=True)

    def __str__(self):
        return self.name.korean

    def sum_of_base_stats(self):
        sum = self.base_hp + \
              self.base_attack + self.base_defense + \
              self.base_special_attack + self.base_special_defense + \
              self.base_speed

        return sum

    def can_learn_moves_order_by_ascending_id(self):
        return self.can_learn_moves.order_by('id')

@deconstructible
class PokemonNature(models.Model):
    name = models.OneToOneField(Name, on_delete=models.CASCADE)
    increased_stat = models.ForeignKey(Name, on_delete=models.CASCADE, related_name='+')
    decreased_stat = models.ForeignKey(Name, on_delete=models.CASCADE, related_name='+')

    def __str__(self):
        return self.name.korean