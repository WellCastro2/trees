from django.db import models
from django.contrib.auth.models import User

from core.common.base import BaseModel


class User(User):

    class Meta:
        proxy = True

    def plant_tree(self, tree, loc, age, account=None):
        '''Create new planted tree and return object'''

        tree, created = Tree.objects.get_or_create(
            name=tree,
            defaults={'scientific_name': tree},
        )

        return PlantedTree.objects.create(
            age=age,
            user=self,
            tree=tree,
            lat=loc[0],
            long=loc[1],
            account=account
        )

    def plant_trees(self, plants: list, account=None):
        '''Create list new planted tree and return objects createds'''

        create_list = []

        for obj in plants:

            tree_name = obj[0]
            loc = obj[1]

            obj_tree, created = Tree.objects.get_or_create(
                name=tree_name,
                defaults={'scientific_name': tree_name},
            )
            create_list.append(PlantedTree(
                user=self,
                tree=obj_tree,
                lat=loc[0],
                long=loc[1],
                account=account
            ))

        planted_trees = PlantedTree.objects.bulk_create(create_list)

        return planted_trees

    def get_planted_trees(self):
        '''Return all planteds trees user'''
        return PlantedTree.objects.filter(user=self)

    def get_accounts(self):
        '''Return all accounts user'''
        return Account.objects.filter(users=self)

    @property
    def planteds_count(self):
        '''Return total planteds tree user'''
        return self.get_planted_trees().count()


class Account(BaseModel):
    name = models.CharField('Name', max_length=100)
    users = models.ManyToManyField(User, blank=True, related_name='accounts')
    active = models.BooleanField('Active', default=True)

    def __str__(self):
        return self.name


class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField(max_length=500, blank=False)

    def __str__(self):
        return self.user.first_name


class Tree(BaseModel):
    name = models.CharField('Name', max_length=100)
    scientific_name = models.CharField('Scientific Name', max_length=150)

    def __str__(self):
        return self.name


class PlantedTree(BaseModel):
    age = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="plantedtree_set")
    tree = models.ForeignKey(Tree, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True)
    lat = models.DecimalField(max_digits=10, decimal_places=8, blank=False, null=False)
    long = models.DecimalField(max_digits=11, decimal_places=8, blank=False, null=False)

    def __str__(self):
        return self.tree.name
